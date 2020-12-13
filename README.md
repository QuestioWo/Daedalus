A maze generating and rendering program using recursive backtracking written in Sigma16. This was written cause I was bored during the exam diet and needed something to do. It also served as a way of better testing the [Sigma17](https://questiowo.github.io/Sigma17) emulator.

## Running
This atrocious program can be ran by copying the `S16MazeGenerator.asm.text` file into the text area in the `Editor` tab of the [Sigma16 emulator](https://questiowo.github.io/Sigma17). This program was only written for use in [this](https://questiowo.github.io/Sigma17) emulator as it was easier than capitalising every "r". It can be made to run in the original emulator by exporting it to Raw Compatible using the down-arrow next to the Download button on the same Editor tab. I wouldn't recommend it, I'd guess it'd take forever and a day.

## Changing the output
The output of the maze will be the same for each running, unless some constant values are changed. 

The values that can be changed without incident are `height`, `width` and `seed`. These can all be found at the bottom of the file denoted by the `parameters` comment on line `724`. The `seed` will change the maze design as it changes the random number generator's seed. The `width` and `height` will, of course, change the widths and heights of the mazes generated. There will exist combinations of maximum widths and heights but these have not been found yet.

## `main.py`
This contains a python version of the Sigma16 program for better understanidn of the program. This can be ran using `python3 main.py` and requires no extra libraries. It can be modified in a similar way to Sigma16 version; changing the values of the `width`, `height`, and `seed` variables.

## Author

This Sigma16 program was written by [Jim Carty](https://questiowo.github.io). Email: cartyjim1@gmail.com

## License

This project is licensed under the terms of the MIT license. See `LICENSE.txt` for the full license.
