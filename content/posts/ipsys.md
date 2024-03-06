+++
title = 'IPSYS - Particle system with nice random laws in C & OpenGL'
date = 2024-03-06T18:51:08+01:00
draft = false
tags = ['C', 'OpenGL']
image = "/ipsys-saves-21.png"
+++

Visualizer of a particle system with randomized interaction laws that often happen to be quite mesmerizing to contemplate. Fast, colorful and somewhat intresting.

[GitHub repository](https://github.com/anima-libera/ipsys)

# Features

- Particle system that runs on the GPU in a compute shader.
- Different particle types, the number of which is decided at launch time.
- Interaction laws for each oriented pair of particle types:
  - The interaction laws depend on the distance between the interactee and the interacter particles.
  - There are multiple laws for each oridented pair:
    - A law that dictates attraction/repultion,
	- a law that dictates rotation to the left/right, and
	- a law that dictates acceleration/deceleration.
- Interaction law randomizer, carefully tweaked to maximize "intresting" results occurences.
- Randomized colors for each partcile type, color changing with speed and pressure (number of overlaping other particles).
- Fading effect that leaves a tail behind particles
- Saving/loading to/from disk laws, colors and state, written in a custom file format.
- Grounds for a widget tree that is actually be maintainable in C.

# Gallery

![Image of an Ipsys system.](/ipsys-saves-01.png)
![Image of an Ipsys system.](/ipsys-saves-02.png)
![Image of an Ipsys system.](/ipsys-saves-03.png)
![Image of an Ipsys system.](/ipsys-saves-04.png)
![Image of an Ipsys system.](/ipsys-saves-05.png)
![Image of an Ipsys system.](/ipsys-saves-06.png)
![Image of an Ipsys system.](/ipsys-saves-07.png)
![Image of an Ipsys system.](/ipsys-saves-08.png)
![Image of an Ipsys system.](/ipsys-saves-09.png)
![Image of an Ipsys system.](/ipsys-saves-10.png)
![Image of an Ipsys system.](/ipsys-saves-11.png)
![Image of an Ipsys system.](/ipsys-saves-12.png)
![Image of an Ipsys system.](/ipsys-saves-13.png)
![Image of an Ipsys system.](/ipsys-saves-14.png)
![Image of an Ipsys system.](/ipsys-saves-15.png)
![Image of an Ipsys system.](/ipsys-saves-16.png)
![Image of an Ipsys system.](/ipsys-saves-17.png)
![Image of an Ipsys system.](/ipsys-saves-18.png)
![Image of an Ipsys system.](/ipsys-saves-19.png)
![Image of an Ipsys system.](/ipsys-saves-20.png)
![Image of an Ipsys system.](/ipsys-saves-21.png)
![Image of an Ipsys system.](/ipsys-saves-22.png)

![Image of an Ipsys system.](/ipsys-00.png)
![Image of an Ipsys system.](/ipsys-02.png)
![Image of an Ipsys system.](/ipsys-03.png)
![Image of an Ipsys system.](/ipsys-04.png)
![Image of an Ipsys system.](/ipsys-05.png)
![Image of an Ipsys system.](/ipsys-06.png)
![Image of an Ipsys system.](/ipsys-07.png)
![Image of an Ipsys system.](/ipsys-08.png)
![Image of an Ipsys system.](/ipsys-09.png)
![Image of an Ipsys system.](/ipsys-10.png)
![Image of an Ipsys system.](/ipsys-11.png)
![Image of an Ipsys system.](/ipsys-12.png)
![Image of an Ipsys system.](/ipsys-13.png)
![Image of an Ipsys system.](/ipsys-14.png)
![Image of an Ipsys system.](/ipsys-15.png)
![Image of an Ipsys system.](/ipsys-16.png)
![Image of an Ipsys system.](/ipsys-17.png)
![Image of an Ipsys system.](/ipsys-18.png)
![Image of an Ipsys system.](/ipsys-19.png)
![Image of an Ipsys system.](/ipsys-20.png)
![Image of an Ipsys system.](/ipsys-21.png)
![Image of an Ipsys system.](/ipsys-22.png)
![Image of an Ipsys system.](/ipsys-23.png)
![Image of an Ipsys system.](/ipsys-24.png)
![Image of an Ipsys system.](/ipsys-25.png)
![Image of an Ipsys system.](/ipsys-26.png)
![Image of an Ipsys system.](/ipsys-27.png)
![Image of an Ipsys system.](/ipsys-28.png)
![Image of an Ipsys system.](/ipsys-29.png)
![Image of an Ipsys system.](/ipsys-30.png)
![Image of an Ipsys system.](/ipsys-31.png)
![Image of an Ipsys system.](/ipsys-32.png)
![Image of an Ipsys system.](/ipsys-33.png)
![Image of an Ipsys system.](/ipsys-34.png)
![Image of an Ipsys system.](/ipsys-35.png)
![Image of an Ipsys system.](/ipsys-36.png)

# A few gifs

![Gif of an Ipsys system.](/ipsys-01.gif)
![Gif of an Ipsys system.](/ipsys-37.gif)
![Gif of an Ipsys system.](/ipsys-38.gif)
![Gif of an Ipsys system.](/ipsys-39.gif)

