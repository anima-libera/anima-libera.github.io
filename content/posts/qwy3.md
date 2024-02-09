+++
title = 'Qwy3 - WIP Minecraft-like in Rust with Wgpu'
date = 2024-02-08T17:05:05+01:00
draft = true
tags = ['Rust', 'Wgpu']
image = "/qwy3-crop-name.png"
+++

Work in progress Minecraft-like. This project intends to serve as a base to experiment with procedural generation a bit more than what is usually done in Minecraft-likes. This page will only present what is already implemented and will not focus of the future of this project (for which I have so many ideas).

[GitHub repository](https://github.com/anima-libera/qwy3)

## Key features

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

## On intresting and fast terrain generation

### Using noise

There are multiple world generators available, most of which generate terrain by manipulating 2D and 3D noise.

![Image of some terrain generation that uses noise to shape the terrain.](/qwy3-01.png)

#### Nice properties

We want terrain that generates in a way that does not depend:
- on the order in which the chunks generate,
- nor on the size of the chunks,
- nor on the offset of the chunk grid (the placing of the chunk edges).

These constraints allow to consider that the world would always generate in the same way not matter the other settings or implementation details, instead of a generation that is influenced by the player's actions. Most people would not care about these properties but I want to see the worlds of Qwy3 as exisiting independently from the player's actions.

Using transformed noise to generate each block of the world guarentees that the terrain generation has these properties because the generator can be expressed as a function that maps block coordinates to a block type. The generation of each block is independant from the generation of all the other blocks, no matter the size, position and loading order of the chunks.

#### What can we do with noise

Using N-dimensional noise and transforming it in original ways can make for intresting terrain that break the monotony of 2D height map style terrain. For starters, 3D noise allows for overhangs to appear which doesn't happen with 2D height maps. It also allows for floating islands (which can be desirable or not depending on the feel we aim for the game). But it can allow for so much more!

Here is an example of multiple 3D noises being used to generate curved lines in 3D, could be used as a base for the generation of some future aerial biomes (when biomes will be implemented):

![Other image of some terrain generation that uses noise to shape the terrain.](/qwy3-02.png)

### Structures

**Comming soon**

### Chunk culling and loading order

**Comming soon**
