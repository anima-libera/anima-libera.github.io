+++
title = 'Custom Build System for C/C++ in Python'
date = 2024-03-06T18:50:08+01:00
draft = false
tags = ['Python', 'C', 'C++']
+++

Handmade build system for C/C++ executable projects, made in Python.

<!--more-->

# Features

- Creating new source files warrant no modification of the build system.
- Incremental compilation, keeps artifacts and recompile only the translation units that have changed.
- Parses source files for `#include`s to make an inclusion graph and propagate changes in headers down the graph to flag all concerned translation units for recompilation correctly.
- The inclusion graph can be converted to a DOT file.
- Allows a special header to contain special custom declarations that trigger code generation to embed text/binary ressources in the binary.
- Allows to run the compiled binary after compilation, but only if compilation worked.
- Different compilation options produce artifacts that are stored separately so as to reproduce compilation profiles.
- Easy to tweak to the needs of the project, that was the whole point of making a custom build system.

# Why? Why not just use CMake or Make?

The standard for C and C++ projects is to use CMake, or sometimes just Make. Some benefits are to be gained from such decision, for example some features such as parallel compilation, or the fact that some libraries include a bit of CMake script that is meant to ease its use as a dependency in CMake projects.

In my humble opinion, these benefits do not outweight the inconvenience of how hard it is to understand the obscure ways by which these build systems are indended to be used and configured. If it is quite easy to get them to work on a project by copy-pasting the words of power from StackOverflow into our project, it often remains too mysterious (at least for me) to troubleshoot issues or tweak.

In the end, the build system for a project is just a program that handles the efficient management of the compiling process. I understand that some domain specific language can make the writing and maintenance of such program easier by providing language features related to file and compilation handling. I do not think that being a domain specific language is an excuse to be so uncomfortable and hard to use as the DSLs of CMake and Make. Using a more classic general purpose programming language such as Python is so much nicer, with the small price of having to reimplement some features by hand.

The build system is an important detail of a C/C++ project; a detail, but an important one. I felt more confident in the future of these projects knowing that I fully understood the build system and could tweak/augment/fix it to make it fit to the needs of the project. Using a proper language also allows to augment the build system with features such as code generation, that I believe even a master of CMake script would have a hard time to implement in such an impractical language.

*Note*: This custom build system was used on personal hobby projects, where I thought it made sense. In a team of enough people, the fact that some solution is an industry standard makes it more relevant due to being known (to some extent) by all the team. I may find it intresting to design a custom writing system if there were no other humans to read it, but since there are other humans to communicate with then the standard writing system shared by everyone has more value.

# Where is it used?

There is no standalone version of this build system, it was copy-pasted in new projects and tweaked accordingly.

- [Here](https://github.com/anima-libera/qwy2/tree/6be3c50bba2e2fcde6e47e67a4b8273bd836b2ce/buildsystem) it is used in [Qwy2]({{< ref "posts/qwy2" >}}) (C++ project), one can see the use of code generation triggered by the special declarations in [this special header](https://github.com/anima-libera/qwy2/blob/6be3c50bba2e2fcde6e47e67a4b8273bd836b2ce/src/embedded.hpp) to embed some ressources in the binary.

The other projects it was used in did not make it to this portfolio due to not being presentable enough due to being abandoned too soon.

- [Here](https://github.com/anima-libera/WhyCrystals-abandoned-2/tree/13c518f35dc117efe8e8cde31050be757cac7a6a/buildsystem) it is used in an abandoned C project that I happened to have posted on GitHub, with the code generation for ressource embedding being triggered by [this special header](https://github.com/anima-libera/WhyCrystals-abandoned-2/blob/13c518f35dc117efe8e8cde31050be757cac7a6a/src/embedded.h).
