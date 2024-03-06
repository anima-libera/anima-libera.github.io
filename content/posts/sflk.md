+++
title = 'SFLK - Interpreted programming language implemented in Rust'
date = 2024-03-06T18:48:08+01:00
draft = false
tags = ['Rust']
image = "/sflk-00.png"
+++

Trying their hand at "making their own programming language" is common place among programmers. My attempt at an interpreted language aimed at trying new things instead of focussing on speed, having fun instead of believing that my language would attract any intrest, there are hundreds of new languages each months after all.

[GitHub repository](https://github.com/sflk-lang/sflk)

# Features

- Handmade tokenizer and parser.
- Handmade implementation of [big integers and arbitrarily precise fractions](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic) (!!), with unit tests. Can be seen [here](https://github.com/sflk-lang/sflk/blob/849f8b1571475e25f14017ff61d7d65bfd6fc40f/sflk-lang/src/bignums.rs).
- Algebraic effects, which I only learned about after implementng them (they are called "signals" in SFLK). All side effects executed by a scope can be intercepted by an outer scope with full control about what to do with it and how to respond.
- Bytecode.
- Visualizer of the AST and of the program execution (with scopes visible as gutter indentations).
- Grounds for the pretty printing of remarks about the program.
- Original design in some syntactical and semantical aspects of the language (most of which are for fun, to try something new regardless of usefulness or relevancy):
  - No statement separator, ignored whitespace and two-letters keywords make for concise scripts.
  - Arbitrary number and order of "then" and "else" branches of if statements, same goes for some other clauses of other statements such as loop body and such.
  - Loop separator clause that runs inbetween iterations of the loop body.
  - Blocks of code are expressions, first-class values that can be executed in the current scope or in a sub-scope, they can be concatenated together or repeated, they replace functions.
  - Variable table of a scope can be copied, manipulated and poored in a scope, they replace hashmaps with identifier strings as keys.
  - Method-chain-like precedence for expressions involving binary operators.
  - Syntax error that disturb even the parser are "ignored" in that they are ebedded in the AST and as long as they are not executed then no error is raised. Debugging tools in the intrepreted allow to still see these errors as it would be hard to debug otherwise.
- A README explaning all the language quirks and features.

# Why?

For fun!

# Gallery

Here can be seen the pretty printed AST of an SFLK program, and the pretty printing of its execution with scope visualization:

![Image of an SFLK program AST and detailed execution.](/sflk-01.png)

Here can be seen an SFLK program containing a loop statement that has a separaror clause (`sp` keyword followed by a statement) which makes it trivial to print a separation between the prints of each iteration:

![Image of an SFLK loop with a separator statement.](/sflk-02.png)

Here can be seed an SFLK program working with big integers, and then an SFLK program working with arbitrarily precise fractions:

![Image of an SFLK program working with big integers.](/sflk-03.png)
![Image of an SFLK program working with arbitrarily precise fractions.](/sflk-04.png)

Here can be seen tests of a pretty-printer of remarks on the program:

![Image of an SFLK program selected intervals being pretty-printed with notes.](/sflk-05.png)
![Image of an SFLK program selected intervals being pretty-printed with notes.](/sflk-06.png)
![Image of an SFLK program selected intervals being pretty-printed with notes.](/sflk-07.png)

Here can be seen an SFLK program outputing an image in [PPM format](https://en.wikipedia.org/wiki/Netpbm#File_formats):

![Image of an SFLK program outputing an image.](/sflk-08.png)
![Image of an SFLK program output read as the PPM image it is.](/sflk-09.png)

Here can be seen an SFLK program defining and then using a "signal interceptor" (which happens to really be just an effect handler actually):

![Image of an SFLK program defining a "signal interceptor" (an effect handler).](/sflk-10.png)
![Image of an SFLK program using that interceptor.](/sflk-11.png)
