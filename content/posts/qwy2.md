+++
title = 'Qwy2 - Previous Minecraft-like attempt in C++ & OpenGL'
date = 2024-03-06T18:53:08+01:00
draft = false
tags = ['C++', 'OpenGL']
image = "/qwy2-00.png"
toc = true
+++

The previous Minecraft-like attempt before [Qwy3]({{< ref "posts/qwy3" >}}).

[GitHub repository](https://github.com/anima-libera/qwy2)

# Features

- Infinite world in all directions including up and down, thanks to cubic chunks.
- Chunk meshing with covered face culling and ambiant occlusion trick.
- Multiple procedural terrain generators.
- Home made noise computation with up to 3 floating point dimensions and 1 integer dimpension.
- Blocks can be placed and removed.
- Saving/loading to/from named saves on disk. Can save every generated chunks or only the ones that underwent change.
- Threadpool for terrain generation (different steps in different tasks), loading from disk, initial meshing (but not remeshing).
- Grounds for entities (some throwable spinning crystals as tests are implemented).
- Dynamic shadows by shadow mapping (not cascading).
- Fog effect (that only works because the sky is one uniform color instead of an arbitrary skybox).
- Procedurally generated block textures (less intresting than Qwy3's).
- Configurable controls for most controls.
- Grounds for a stripting language.
- Configurable chunk size at launch time. (Actually useful as this parameter influences the performance of the generation, gameloop and memory usage in complex ways and the best value that optimizes for what a given user prefers on a given machine may be different from one another, and it doesn't cost anything to make this a parameter.)
- [Custom build system]({{< ref "posts/buildsystem" >}}) for better control of the build process, with code generation for ressource embedding.

# Gallery

![Image of some Qwy2 world with the classic generator.](/qwy2-01.png)
![Image of some Qwy2 world with a sky lines biome near a solid biome.](/qwy2-02.png)
![Image of some Qwy2 world with two biomes near some empty sky.](/qwy2-03.png)
![Image of some Qwy2 world with multiple biomes.](/qwy2-04.png)
![Image of some Qwy2 flat-ish world with a handmade small amongus crewmate statue.](/qwy2-05.png)

# Why the Qwy3 rewrite?

Since learning [Rust](https://www.rust-lang.org/) (memory safe, no undefined behavior, super clean language features and type system, [fearless concurrency (!)](https://doc.rust-lang.org/book/ch16-00-concurrency.html), standard package manager, etc.) and hearing about [Wgpu](https://wgpu.rs/) (*safe graphics API* implemented in Rust, [WGSL](https://www.w3.org/TR/WGSL/) (clean shader language), Vulkan backend to use its validation layers), I thought more and more about the state of Qwy2, stuck with old technologies (C++ and OpenGL, full of undefined behavior, legacy and inelegant features) and how much easier the development would have been if it was made in Rust & Wgpu since the beginning. In addition, I was unhappy with some technical decisions made for Qwy2 (for example the fact that there are multiple generation steps for each chunks, making generation very slow), and a rewrite would allow to benefit from these mistakes to make it better.

So far, I believe that the [Qwy3]({{< ref "posts/qwy3" >}}) rewrite in Rust & Wgpu was the best decision regarding this project. Qwy2 shall remain in its unfinished state as the previous iteration of Qwy3. Third time's a charm!
