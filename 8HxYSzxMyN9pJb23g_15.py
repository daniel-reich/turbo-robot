"""


Create a function that accepts `txt` and `cases` as parameters where the
string is split into **N distinct cases** of **equal length** as shown:

### Examples

    split_n_cases("Strengthened", 6) ➞ ["St", "re", "ng", "th", "en", "ed"]
    
    split_n_cases("Unscrupulous", 2) ➞ ["Unscru", "pulous" ]
    
    split_n_cases("Flavorless", 1) ➞ ["Flavorless" ]

### Notes

If it's not possible to split the string as described, return `["Error"]`.

"""

def split_n_cases(txt, cases):
  if cases > len(txt):
    return ["Error"]
  elif len(txt) % cases != 0:
    return ["Error"]
  else:
    segment_length = len(txt) / cases
    split_list = []
    x = 0
    y = int(segment_length)
    for i in range(cases):
      split_list.append(txt[x:y])
      x += int(segment_length)
      y += int(segment_length)
  return split_list

