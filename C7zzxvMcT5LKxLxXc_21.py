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
  lol = "defghijklmnopqrstuvwxyzabc"
  lst = []
  ok = 0
  for x in txt:
    print(x)
    if x == " ":
      lst.append(5)
      ok += 1
    if x == "R":
      lst.append(10)
      ok += 1
    if ok >= 1:
      ok = 0
    elif lol.index(x) + 1 <= 10:
      lst.append(lol.index(x) + 1)
    elif lol.index(x) + 1 <= 20:
      lst.append(lol.index(x) + 1 - 10 + 1)
    elif lol.index(x) + 1 <= 23:
      lst.append(lol.index(x) + 1 - 20 + 2)
    else:
      lst.append(lol.index(x) + 1 - 10 + 2)
  print(lst)
  return lst

