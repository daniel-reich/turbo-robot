"""


The **centered polygonal numbers** are a family of sequences of 2-dimensional
figurate numbers, each formed by a central dot, surrounded by polygonal layers
with a constant number of sides. Each side of a polygonal layer contains one
dot more than a side in the previous layer.

![](https://edabit-
challenges.s3.amazonaws.com/CenteredTriangularNumber_1.png)|
![](https://edabit-challenges.s3.amazonaws.com/CenteredSquareNumber_2.png)  
---|---  
Centered triangular numbers| Centered square numbers  
![](https://edabit-
challenges.s3.amazonaws.com/CenteredPentagonalNumber_3.png)|
![](https://edabit-challenges.s3.amazonaws.com/CenteredHexagonalNumber_4.png)  
Centered pentagonal numbers| Centered hexagonal numbers  
  
In the following table are listed the first 12 terms of the sequences of
centered _k_ -polygonal numbers, with _k_ from 3 to 22:

k| Name| 0| 1| 2| 3| 4| 5| 6| 7| 8| 9| 10| 11  
---|---|---|---|---|---|---|---|---|---|---|---|---|---  
3| Triangular| 1| 4| 10| 19| 31| 46| 64| 85| 109| 136| 166| 199  
4| Square| 1| 5| 13| 25| 41| 61| 85| 113| 145| 181| 221| 265  
5| Pentagonal| 1| 6| 16| 31| 51| 76| 106| 141| 181| 226| 276| 331  
6| Hexagonal| 1| 7| 19| 37| 61| 91| 127| 169| 217| 271| 331| 397  
7| Heptagonal| 1| 8| 22| 43| 71| 106| 148| 197| 253| 316| 386| 463  
8| Octagonal| 1| 9| 25| 49| 81| 121| 169| 225| 289| 361| 441| 529  
9| Nonagonal| 1| 10| 28| 55| 91| 136| 190| 253| 325| 406| 496| 595  
10| Decagonal| 1| 11| 31| 61| 101| 151| 211| 281| 361| 451| 551| 661  
11| Hendecagonal| 1| 12| 34| 67| 111| 166| 232| 309| 397| 496| 606| 727  
12| Dodecagonal| 1| 13| 37| 73| 121| 181| 253| 337| 433| 541| 661| 793  
13| Tridecagonal| 1| 14| 40| 79| 131| 196| 274| 365| 469| 586| 716| 859  
14| Tetradecagonal| 1| 15| 43| 85| 141| 211| 295| 393| 505| 631| 771| 925  
15| Pentadecagonal| 1| 16| 46| 91| 151| 226| 316| 421| 541| 676| 826| 991  
16| Hexadecagonal| 1| 17| 49| 97| 161| 241| 337| 449| 577| 721| 881| 1057  
17| Heptadecagonal| 1| 18| 52| 103| 171| 256| 358| 477| 613| 766| 936| 1123  
18| Octadecagonal| 1| 19| 55| 109| 181| 271| 379| 505| 649| 811| 991| 1189  
19| Enneadecagonal| 1| 20| 58| 115| 191| 286| 400| 533| 685| 856| 1046| 1255  
20| Icosagonal| 1| 21| 61| 121| 201| 301| 421| 561| 721| 901| 1101| 1321  
21| Icosihenagonal| 1| 22| 64| 127| 211| 316| 442| 589| 757| 946| 1156| 1387  
22| Icosidigonal| 1| 23| 67| 133| 221| 331| 463| 617| 793| 991| 1211| 1453  
  
As you can see:

  * 6 is the 1st _pentagonal number_.
  * 16 is the 2nd _pentagonal number_ and the 1st _pentadecagonal number_.
  * 19 is the 3rd _triangular number_ , the 2nd _hexagonal number_ and the 1st _octadecagonal number_.

Write a function that takes an integer `n` as argument and returns its
classification as polygonal number:

  * return `"0th of all"` if `n` is 1, since it is the 0th term of every centered polygonal number sequence.
  * return a list whose generic element is a string formatted as `"{i}th {k}-gonal number"` if `n` is the _i_ -th _k_ -gonal number, in _k_ -ascending order.
  * return `False` if `n` is not a _k_ -gonal number for any _k_ > 2.

### Examples

    is_polygonal(3) ➞ False
    
    is_polygonal(4) ➞ ["1st 3-gonal number"]
    
    is_polygonal(16) ➞ ["2nd 5-gonal number", "1st 15-gonal number"]

### Notes

N/A

"""

def is_polygonal(n):
  if n == 1: return '0th of all'
  K = []
  for i in range(n, 0, -1):
    k = round(2 / i / (i + 1) * (n - 1), 9)
    if k > 2 and k % 1 == 0: K += ["%s %d-gonal number" % (
      str(i) + 'tsnrhtdd'[i % 5 * (i % 100 ^ 15 > 4 > i % 10)::4], k
    )]
  return K or 0

