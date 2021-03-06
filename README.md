# xmastree

Generate your own Christmas trees by entering some numbers. Ornaments are also generated.


## Dependencies

- Python 3
- `colorama` (for colored output)
- `numpy` (for randomized ornament generation)


## Note

- Make sure you run it in an environment that can display color.


## Input Guide
|      Input Label | Suggested Value | Description                                                                                                          |
|-----------------:|:---------------:|:---------------------------------------------------------------------------------------------------------------------|
|             Rows |       `24`      | Height of the leafy part of the tree.                                                                                |
|          Setback |       `4`       | Amount of "pixels" to subtract for the spiky parts of the steriotypical Christmas tree. Input a 0 to have no spikes. |
|         Interval |       `6`       | Number of rows between the "spiky" parts.                                                                            |
|        Frequency |       `0.1`     | Frequency of the appearance of ornaments.                                                                            |
|     Trunk height |       `3`       | What the `Input Label` says.                                                                                         |
|      Trunk width |       `2`       | ((What the `Input Label` says) -1)/2 *(Actual width will be input\*2 + 1)*                                           |
|       Body color |       `g`       | Color of the leafy part of the tree.                                                                                 |
| Background color |       `k`       | What the `Input Label` says.                                                                                         |
|      Trunk color |       `y`       | What the `Input Label` says.                                                                                         |


## Color guide

| Label |   Color  |
|:-----:|:--------:|
|  `b`  |  Blue    |
|  `c`  |  Cyan    |
|  `g`  |  Green   |
|  `m`  |  Magenta |
|  `r`  |  Red     |
|  `y`  |  Yellow  |
|  `w`  |  White   |
|  `k`  |  Black   |


## Examples

![Example](https://github.com/pythonian23/xmastree/raw/master/screenshot0.png)
![Example](https://github.com/pythonian23/xmastree/raw/master/screenshot1.png)
