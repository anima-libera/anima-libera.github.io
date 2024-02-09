+++
title = 'Qwy3 - WIP Minecraft-like in Rust with Wgpu'
date = 2024-02-08T17:05:05+01:00
draft = false
tags = ['Rust', 'Wgpu']
image = "/qwy3-00.png"
+++

Work in progress Minecraft-like. This project intends to serve as a base to experiment with procedural generation a bit more than what is usually done in Minecraft-likes. This page will only present what is already implemented and will not focus of the future of this project (for which I have so many ideas).

[GitHub repository](https://github.com/anima-libera/qwy3)

# Features

- Infinite world in all directions including up and down, thanks to cubic chunks.
- Chunk meshing with covered face culling and ambiant occlusion trick.
- Multiple procedural terrain generators. Some use a custom structure generation engine that is fast and can handle large structures while keeping the world independent from chunk loading order (see the generator `structures-links-smooth`).
- Home made N-dimensional noise computation.
- Optimized chunk loading order that culls away covered and inaccessible chunks and prioritize terrain over air.
- Blocks can be placed and removed (but this is not saved to disk yet).
- Procedurally generated skybox texture.
- Threadpool for terrain generation, meshing and skybox texture generation.
- Dynamic shadows by shadow mapping.
- Procedurally generated block textures (see the generator `structures-generated-blocks`).
- Configurable controls for most controls.
- Custom widget tree for the interface.
- Grounds for a statically typed stripting language.
- Configurable chunk size at launch time. (Actually useful as this parameter influences the performance of the generation, gameloop and memory usage in complex ways and the best value that optimizes for what a given user prefers on a given machine may be different from one another, and it doesn't cost anything to make this a parameter.)

# On interesting and fast terrain generation

## Using noise

There are multiple world generators available, most of which generate terrain by manipulating 2D and 3D noise.

![Image of some terrain generation mainly based on noise.](/qwy3-01.png)

### Nice properties

We want terrain that generates in a way that does not depend:
- on the order in which the chunks generate,
- nor on the size of the chunks,
- nor on the offset of the chunk grid (the placing of the chunk edges).

These constraints allow to consider that the world would always generate in the same way not matter the other settings or implementation details, instead of a generation that is influenced by the player's actions. Most people would not care about these properties but I want to see the worlds of Qwy3 as exisiting independently from the player's actions.

Using transformed noise to generate each block of the world guarentees that the terrain generation has these properties because the generator can be expressed as a function that maps block coordinates to a block type. The generation of each block is independant from the generation of all the other blocks, no matter the size, position and loading order of the chunks.

### Only one step

Also why not wanting *chunks to generate in **only one step***? Some world generators of other voxel games (and also Qwy2's generation) would have each chunk generate in multiple steps, each step requiring the completion of the previous step for all the neighboring chunks. A problem with such technique is that we end up with a large number of partially generated chunks on the edge of the generated area which we cannot mesh and render to the player because their last generation step cannot be done because it would require to extend the generated area a chunk further and if we do that then we just moved this problem a chunk further. All these generation steps use precious time that is not spent on directly generating the chunks that end up visible to the player, and also use more memory.

Qwy3 generates each chunk in one step, meaning from nothing to block data to meshing without the need for neighboring chunks to even exist (although the meshing is done again when neighboring chunks are generated to make sure that the ambiant occlusion and face culling on the edges of the chunk take into account neighboring blocks from the neighboring chunks). This happens to not be a problem for structure generation, which is explained further below.

### What can we do with noise

Using N-dimensional noise and transforming it in original ways can make for interesting terrain that break the monotony of 2D height map style terrain. For starters, 3D noise allows for overhangs to appear which doesn't happen with 2D height maps. It also allows for floating islands (which can be desirable or not depending on the feel we aim for the game). But it can allow for so much more!

Here is an example of multiple 3D noises being used to generate curved lines in 3D, could be used as a base for the generation of some future aerial biomes (when biomes will be implemented):

![Image of some terrain generation based on noise in an interesting way (I hope!).](/qwy3-02.png)

This is a matter of discovering interesting ways to transform and combine noises and keeping the ones that happen to fit the desired feel of the game. Some terrains like the lines above were not foud by chance but by an intuition about how to get line-like shapes to generate in 3D; however there is no reason to not try random noise manipulations as these sometimes turn out interesting enough.

![Image of some terrain generation based on noise in a wierd way.](/qwy3-03.png)
![Image of some terrain generation based on noise in a way discovered by chance.](/qwy3-04.png)

## Structures

Transformed 3D noise is not enough! Blocks are related to eachother only by proximity in the noise sampling. How to generate trees this way? It may be possible by carefully tweaking impossibly complex noise transformations for weeks or even months, but I would not resort to such cumbersome way.

We want to be able to describe structure generation as a sequential algorithm, using operations such as "place a block there", "fill a sphere of such radius there", etc.

### The chunk edge problem

But what to do when a tree decides to generate near the edge of a chunk and is cut by the edge?

A few solutions that were *not* applied:
- Having multiple generation steps and structures smaller than a chunk is a simple solution, that was *not* applied to Qwy3 because:
  - a constraint on structure sizes that depend on the chunk size means that the world generation is indirectly influenced by the size of chunks, and as said above I refuse to let that parameter limit the generation,
  - as also said above, having a single generation step for chunks is a great advantage that is not to be given up so easily.
- Having the tree be generated anyway by the chunk in which it decided to appear, allowing the tree generation to place blocks outside of the chunk, editing chunks already generated and saving the blocks that are placed on non-generated chunks to be applied on them when they generate is also a solution. It was *not* applied to Qwy3 because:
  - it is harder to do it in a thread-safe way, as the generation of each chunk is done in a separate thread,
  - it allows large structures but generating a large structure (that spans over many chunks) will require the edition of many chunks both for already-generated chunks and for to-be-generated chunks, all that for each chunk that generates a large structure,
  - and if it allows large structures then a sufficiently large structure that is generated by a chunk far away from the player may generate blocks near or on the player; we want the generation to generate a chunk and be done with it, not comming back to already generated chunks to edit them potentially plenty of times.
- Having structures smaller than a chunk and that are generated in a way that makes it so that they do not cross the chunk edges. This solution was *not* applied to Qwy3 because:
  - again, structure sizes shall not be limited by chunk sizes for reasons stated above,
  - and the world generation shall not be influenced by the chunk grid offet (placing of the chunk edges).

### The chunk edge solution

Considering two adjacent chunks that must both generate different parts of the same tree, how can they agree on what to generate so that it matches perfectly at the shared edge that cuts the tree? How can they even know that they must agree on a shared tree?

The way noise-induced terrain works fine across chunk edges is because both chunks sample the same noise functions that happen to be spatially coherent. This coherency can be reproduced for structures. Noise sampling is not limited to floating point parameters and can be done with integer parameters. This allows to map noise values to cells of a cubic lattice (that has a scale that does not depend on the size of chunks). Chunks can now check which cells of the lattice they overlap with and use the noise values from these cells (that are shared with the other chuncks as per the fact that a noise function is deterministic (pure)) to generate parts of structures that occupy these cells. Each chunk generates all the structures that might overlap with it and only keeps the parts that actually overlap with it; structures that might span over multiple chunks are "generated" multiple times, but always at the exact same position and in the exact same way (always seeded by the same noise values) so that all the parts overlaping different chunks match up perfectly.

Here is an example of this technique being used to generate balls. As opposed to terrain generated by transforming some noise, here the noise is simply used to allow chunks to share values in cells of a lattice so that the chunks can agree on what structures can be generated (here, just balls at different positions in the cells of the lattice) so that said structures can cross chunk edges without issue.
![Image of some terrain generation using a noise value lattice to generate balls.](/qwy3-05.png)

Then noise transofmration can be used again to shape such structures to more natural-looking terrain.
![Image of some terrain generation using a noise value lattice to generate sky islands.](/qwy3-06.png)

### Expanding on the idea

The fact that the position and properties of all the stcuture is decided by noise values and queryable by their position means that a structure can be made aware of its neighboring structures and decide to generate accordingly. For example, the structures can link themselves by generating a bridge, both of the two linked structures generating its half of the bridge.

Here is an example of the balls from earlier, all linked together in one direction:
![Image of some terrain generation using a noise value lattice to generate *linked* balls.](/qwy3-07.png)

Two structures can also decide to agree on some properties together, for example two structures can agree to link themselves or not (which is important if we want to generate structures that are not always linked together, if a pair does not agree on being linked or not then one might generate half a bridge and the other not and the bridge may stop awkwardly, which might look bad if such behavior was not intended). For two structures to agree on some properties, they can use noise again, as the (home made) noise used in Qwy3 is N-dimensional it can be sampled in a 6D space at both the coordinates of the structures origins for example, in both order, and combine both noise values in an order-independant way (the mean of two values for example) to get a noise value associated to the pair of structures that they will both agree on (both structures will associate the same noise value to the other of their pair, for each pair).

Here is the example of the balls again, but now they can be linked with all of their 6 direct lattice cell neighbors, they decide to link only sometimes, the bridges have a flat top and the generated shapes are also piped in some noise transofmration to make the bridges look more natural (as far as a latice of bridges in an alien sky go anyway, the whole concept way not be very natural but *if it was natural* then it may look like this more than if it was not transformed using noise):
![Image of some terrain generation using a noise value lattice to generate more links.](/qwy3-08.png)

One more strange-looking take on the idea:
![Image of some terrain generation using a noise value lattice to generate even more links.](/qwy3-09.png)

To compare these structure-using generators to the noise-using line generator mentioned above that generates lines of land in the sky, it appears that:
- the structure-using one may be harder to implement,
- but once implemented the structure-using generator is way easier to control and tweak to get it to generate what we want than the noise-using generator,
- and the structure-using generator expands what is actually possible, for example large lines with a circular cut is not really possible with the noise-using technique.

### More structures!

**TODO**

## Chunk culling and loading order

**TODO**
