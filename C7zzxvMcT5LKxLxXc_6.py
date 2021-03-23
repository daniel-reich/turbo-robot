"""


This is a reverse-coding challenge. Create a function that outputs the correct
list from the input. Use the following examples to crack the code.

### Examples

    decode("hello") ➞ [5, 2, 9, 9, 3]
    
    decode("wonderful") ➞ [11, 3, 2, 1, 2, 6, 3, 9, 9]
    
    decode("something challenging") ➞ [7, 3, 10, 2, 8, 5, 6, 2, 4, 5, 18, 5, 16, 9, 9, 2, 2, 4, 6, 2, 4]

### Notes

N/A

"""

Map = {'a': 16, 'b': 17, 'c': 18, 'x': 3, 'y': 4, 'z': 5, ' ': 5}
for c in range(99, 110):
    Map[chr(c)] = c - 99
for c in range(110, 120):
    Map[chr(c)] = c - 108
for o in range(65, 91):
    c = chr(o)
    Map[c] = Map[c.lower()] + 4
​
def decode(txt):
    ans = [Map.get(c, '?') for c in txt]
    return ans

