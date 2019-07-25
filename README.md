# align_fa

align_fa is a script for checking the differences between the two alignment sequences visually.Through it, you can directly see which points have changed.In addition, the fitting function is also given.K ranges from -1 to 2,-1 means that the two sequences are identical;2 means that the two sequences are '-';0 means that the two sequences are half the same,1 means that the two sequences are completely different.

## Default score matrix

|      |   A   |   T   |   C   |   G   |   -   |
| :--: | :--:  | :--:  | :--:  | :--:  | :--:  |
|   A  |   -1  |   1    |    1   |   1   |   2    |
|   T  |   1   |   -1   |   1   |   1    |    2   |
|   C  |   1   |    1   |   -1   |    1   |    2   |
|   G  |   1   |    1   |    1   |   -1    |    2   |
|   -  |    2  |    2   |   2    |   2     |    2   |

## Blast score matrix

|      |   A   |   T   |   C   |   G   |   -   |
| :--: | :--:  | :--:  | :--:  | :--:  | :--:  |
|   A  |   -5  |   4    |    4   |   4   |   5    |
|   T  |   4   |   -5   |   4   |   4    |    5   |
|   C  |   4   |    4   |   -5   |    4   |    5  |
|   G  |   4   |    4   |    4   |   -5    |    5   |
|   -  |    5  |    5   |   5    |   5     |    5   |

## Example
```
>chr1
tgagtaccaaaccaaggatactgatatattggcagcattc
>chr2
tgactatggaaccaaagatactgatatcttggcagcattc
```
```python
 python work.py -a align.fa -s Default12
```
![](https://i.loli.net/2019/07/24/5d382ae355a0787430.png)
