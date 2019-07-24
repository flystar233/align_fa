# align_fa

align_fa is a script for checking the differences between the two alignment sequences visually.Through it, you can directly see which points have changed.In addition, the fitting function is also given.K ranges from -1 to 2,-1 means that the two sequences are identical;2 means that the two sequences are '-';0 means that the two sequences are half the same,1 means that the two sequences are completely different.

## Score matrix

|      |   A   |   T   |   C   |   G   |   -   |
| :--: | :--:  | :--:  | :--:  | :--:  | :--:  |
|   A  |   -1  |   1    |    1   |   1   |   2    |
|   T  |   1   |   -1   |   1   |   1    |    2   |
|   C  |   1   |    1   |   -1   |    1   |    2   |
|   G  |   1   |    1   |    1   |   -1    |    2   |
|   -  |    2  |    2   |   2    |   2     |    2   |

## Example
```python
 python work.py -a align.fa
```
![](https://raw.githubusercontent.com/flystar233/pic_bed/master/filename.png?token=AE34FB6XPF6UBWXFHMISHOS5HAT7C)
