+++
title = 'Push Dungeon - Roguelike with sokoban-like mechanics in Rust'
date = 2024-03-06T18:49:08+01:00
draft = false
tags = ['Rust']
image = "/pushdg-03.png"
+++

Dungeon crawler on a procedurally generated square-tiled grid with turn-based sokoban-like mechanics. Instead of winning by grinding and having high enough stats, what if we fight by carefully controlling the layout like we win in a sokoban-like puzzle game? Push and pull objects on the grid, anticipate or even bait the enemies in a position in which you win, avoid getting cornered or blocked as the "redo"s (points spent to cancel actions) are limited and as precious as HP, if not more. Death can be undone if there are enough reods left to get back in a non-losing position.

[GitHub repository](https://github.com/anima-libera/pushdg)

# The idea

Instead of having objects in an inventory and being decribed by a wall of stat numbers, here the objects are on the grid and must be pushed or pulled around in a sokoban-like fashion and the stats are replaced by the unique properties of objects.

Agents (the player, the enemies, anything that moves on its own) has a force (for now, 2) that allows them to push at most a equal mass in one move. A rock has a mass of 1 (like most objects), so the player may push at most 2 rocks in one move. The walls are too heavy to be pushed. The enemies and the player are also too heavy to be pushed, so instead of pushing eachother around they must hit each other to lower the other's HP to 0. When pushing fails, objects in the attempted push chain try to interact with what they were pushed against and this may result in a hit if a target has HP and can take damages.

Carefully organizing the layout of a battle to put the enemy in a losing position is the way to go in Push Dungeon. Taking a few hits is fine (there are regen hearts to find), making a few mistakes is fine (it may cost redos, but there are also redo hearts to find), but making too many miskates without enough redos may lead to an unescapable position, which is how a puzzle game with limited redos is lost.

# Features

- Procedural generation of messy dungeon-like maps which often happen to be intresting to play in.
- Multiple objects with different mechanics (key to open doors, vision-blocking walls and pushable bush, see-through gem, shield that deals no damages, sword that deals more damages, pickaxe to break walls, rope that is pullable and can pull an other object, etc.).
- Simple animations when objects move or are moved, damage number simple animations.
- Enemies with a simple move heuristic which already provide intresting challenges when in great numbers and depending on the layout.

# Gallery

![Image of some Push Dungeon game.](/pushdg-01.png)
![Image of some Push Dungeon game.](/pushdg-02.png)
![Image of some Push Dungeon game.](/pushdg-04.png)
![Image of some Push Dungeon game.](/pushdg-05.png)
