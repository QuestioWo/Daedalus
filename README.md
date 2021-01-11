This was written cause I was bored during the exam diet and needed something to do. It also served as a way of better testing the [Sigma17](https://questiowo.github.io/Sigma17) emulator.

## Results 
In the output of the emulator after running this horrid program, there will be an ascii interpretation of the generated maze printed. For a 4x4 maze with the seed `1234`, as is the default when running this project, the below will be printed:

```
*--*--*--*--*
|  |        |
*  *--*--*  *
|        |  |
*--*--*  *  *
|     |  |  |
*  *--*  *  *
|           |
*--*--*--*--*
```

For a more complex example, here is a 16x16 with a seed of `1234` :

```
*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
|  |              |     |                       |
*  *--*--*  *  *--*  *  *  *  *--*--*--*  *--*--*
|        |  |        |  |  |     |        |     |
*--*--*  *  *--*--*--*  *  *--*  *--*--*--*  *  *
|     |  |     |     |  |  |     |     |     |  |
*  *  *  *--*  *  *  *  *  *  *--*  *  *  *--*  *
|  |  |     |  |  |  |     |        |  |  |     |
*  *--*--*  *  *--*  *--*--*--*--*--*  *  *  *  *
|     |     |  |        |           |  |  |  |  |
*  *  *  *--*  *  *--*--*  *  *--*  *  *  *  *  *
|  |  |  |  |  |  |     |  |     |  |     |  |  |
*  *  *  *  *  *  *  *  *  *--*  *--*--*--*  *--*
|  |  |  |     |     |  |     |           |     |
*  *  *  *  *--*  *--*  *  *--*--*--*  *  *--*  *
|  |     |     |     |     |           |  |     |
*  *--*--*--*  *--*--*  *--*  *--*  *--*--*  *  *
|     |     |        |  |  |  |     |     |  |  |
*--*  *  *--*--*--*  *  *  *  *--*--*  *  *  *--*
|     |           |  |     |  |        |  |     |
*  *--*--*  *--*--*  *--*  *  *  *--*--*  *--*  *
|  |        |     |     |  |     |        |     |
*  *  *  *--*  *  *--*  *--*--*--*  *--*--*  *--*
|  |  |        |  |     |        |  |     |     |
*  *--*--*--*  *  *  *--*  *--*  *  *  *  *--*  *
|           |  |  |  |     |     |  |  |        |
*--*--*--*  *  *  *  *  *--*--*  *  *  *--*--*  *
|           |  |        |     |     |     |     |
*  *--*--*--*--*--*--*  *  *  *--*  *--*  *  *--*
|        |           |  |  |  |     |     |     |
*--*--*  *  *--*--*  *--*  *  *--*--*  *--*--*  *
|           |              |           |        |
*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*
```

## Running
This atrocious program can be ran by copying the [Daedalus.asm.txt](https://raw.githubusercontent.com/QuestioWo/MazeGeneratorSigma16/main/Daedalus.asm.txt) file into the text area in the `Editor` tab of the [Sigma16 emulator](https://questiowo.github.io/Sigma17). This program was only written for use in [this](https://questiowo.github.io/Sigma17) emulator as it was easier than using the original.

It can be made to run in the original emulator by exporting it to Raw Compatible using the down-arrow next to the Download button on the same Editor tab. You will also have to remove line `3` as the copyright symbol is invalid in the orignal.

## Changing the output
The output of the maze will be the same for each running, unless some constant values are changed. 

The values that can be changed without incident are `height`, `width` and `seed`. These can all be found at the bottom of the file denoted by the `parameters` comment on line `733`. The `seed` will change the maze design as it changes the random number generator's seed. The `width` and `height` will, of course, change the widths and heights of the mazes generated. 

There does exist combinations of maximum widths and heights. As of v1.1, that limit is a number of cells of around 7211 cells. This is due to the program taking `0x279`, aka 633 cells of memory, and each additional cells requiring nine cells of memory as well - 2 for its position in the stack and 7 for its coordinate and boolean wall values. this limit can be achieved by running the program with the parameters of `height` = 1 and `width` = 7211, using up to and including `0xfff9`. Alternatively, for a more interesting maze than just a corridor, a maze of size 84x85 can be used as the parameters, using up to and including `0xfd7a`.

## `main.py`
This contains a python version of the Sigma16 program for better understanding of the program. This can be ran using `python3 main.py` and requires no extra libraries. It can be modified in a similar way to Sigma16 version; changing the values of the `width`, `height`, and `seed` variables.

## Author

This Sigma16 program was written by [Jim Carty](https://questiowo.github.io). Email: cartyjim1@gmail.com

## License

This project is licensed under the terms of the MIT license. See `LICENSE.txt` for the full license.
