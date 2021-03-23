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

def decode(txt):
  lst = [list(int(y) for y in " ".join(str(ord(i))).split(" ")) for i in txt]
  print(lst)
  lst2 = [sum(i) for i in lst]
  print(lst2)
  return lst2

