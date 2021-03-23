"""


The nesting of lists can be viewed indirectly as curves and barriers of the
real data embedded in lists, thus, defeats the very purpose of directly
accessing them thru indexes and slices. In this challenge, a function is
required to **flatten those curves** (i.e. level, iron, compress, raze,
topple) and expose those data as a **single list** and not as a _list of
lists_.

### Examples

    flatten([[[[[["direction"], [372], ["one"], [[[[[["Era"]]]], "Sruth", 3337]]], "First"]]]])
    ➞ ["direction", 372, "one", "Era", "Sruth", 3337, "First"]
    
    flatten([[4666], [5394], [466], [[["Saskia", [[[[["DXTD"]], "Lexi"]]]]]]])
    ➞ [4666, 5394, 466, "Saskia", "DXTD", "Lexi"]
    
    flatten([[696], ["friend"], ["power"], [[[["Marcus"]]]], ["philus"]])
    ➞ [696, "friend", "power", "Marcus", "philus"]
    
    flatten([[["deep"], [[["ocean"]]], [["Marge"]], ["rase", 876]]])
    ➞ ["deep", "ocean", "Marge", "rase", 876]

### Notes

  * There are no empty lists to handle.
  * You're expected to solve this challenge using a **recursive approach**.
  * You can read on more topics about recursion (see **Resources** tab) if you aren't familiar with it yet or haven't fully understood the concept behind it before taking up this challenge.

"""

def flatten(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Parameters.append([])
    
  Draft_One = Parameters[0]
  Draft_Two = Parameters[1]
  
  Embedded = 0
  Counter = 0
  Length = len(Draft_One)
  
  while (Counter < Length):
    Item = Draft_One[Counter]
    Category = type(Item)
    
    if (Category == list):
      Draft_Two.extend(Item)
      Embedded += 1
      Counter += 1
    else:
      Draft_Two.append(Item)
      Counter += 1
  
  if (Embedded == 0):
    return Draft_Two
  else:
    Draft_One = Draft_Two
    Draft_Two = []
    return flatten(Draft_One, Draft_Two)

