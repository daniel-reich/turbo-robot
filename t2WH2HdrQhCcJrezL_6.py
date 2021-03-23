"""


Create a function that returns the list of numbers from a given range. But for
multiples of three, return `“Eda”` instead of the number and for the multiples
of five, return `“Bit”`. For numbers which are multiples of both three and
five, return `“EdaBit”`.

### Examples

    eda_bit(0, 10) ➞ ["EdaBit", 1, 2, "Eda", 4, "Bit", "Eda", 7, 8, "Eda", "Bit" ]
    
    eda_bit(14, 20) ➞ [14,  "EdaBit", 16, 17,  "Eda", 19, "Bit" ]
    
    eda_bit(99, 106) ➞ ["Eda", "Bit", 101, "Eda", 103, 104, "EdaBit", 106 ]

### Notes

In case the number 0 happens to be in the range, return `"EdaBit"` as well.

"""

def eda_bit(start, end):
  temp = []
  for i in range(start,end+1):
    if i % 15 == 0:
      temp.append('EdaBit')
    elif i % 5 == 0:
      temp.append('Bit')
    elif i % 3 == 0:
      temp.append('Eda')
    else:
      temp.append(i)
  return temp

