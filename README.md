# brainfuck-python
Extremely minimalistic Brainfuck python compiler

## Introduction
Brainfuck is a esoteric programming language created in 1993 by Urban Müller. What makes it unique is that it only uses 8 operators, ```<>+-[].,```. While this might seem simple and easy, don't be fooled. Printing even one character requires a lot of time, and trying to make a program, while is possible, gives you a 'brainfuck', hence the name.

## Commands
Brainfuck is known to be extremely minimalistic, with only 8 operators. In Brainfuck, there are containers, called blocks. These blocks can store one number, in ASCII format. A pointer indicates which block is being edited.
```
> = This moves the pointer one block to the right
< = This moves the pointer one block to the left
+ = This increases the value in the block by one
- = This decreases the value in the block by one
[ and ] = This is a while loop. It will keep looping until the value in the block reaches one
, = inputs one character
. = prints one character
```
#### IMPORTANT
- When the program starts, all blocks are set to zero
- The pointer always starts at the leftmost block
- Anything that isn't one of the 8 operators will be treated as a comment
