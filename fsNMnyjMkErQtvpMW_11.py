"""


 _What do the numbers 4, 6, 8, 9 and 0 have in common? They all have holes in
them! Notice how the number 8 contains not one, but two holes._

Given a list of numbers, sort the list in accordance to how many holes occur
in the number. It should be sorted in **ascending order**.

### Examples

    holey_sort([44, 4, 444, 4444]) ➞ [4, 44, 444, 4444]
    
    holey_sort([100, 888, 1660, 11]) ➞ [11, 100, 1660, 888]
    
    holey_sort([8, 121, 41, 66]) ➞ [121, 41, 8, 66]

### Notes

  * If two numbers have the same number of holes in them, sort them by the order they first appeared in.
  * Despite the number 0 appearing to have _two holes_ in certain fonts, it will only have **one hole** for the purposes of this challenge.

"""

def holey_sort(lst):
  
  Values = lst
  
  # Establishing Number of Holes in Each Item of Values
  
  Occurrences = []
  
  VC = 0
  VL = len(Values)
  
  while (VC < VL):
    
    Text = str(Values[VC])
    Holes = 0
    
    Count_Zero = Text.count("0")
    Count_Four = Text.count("4")
    Count_Six = Text.count("6")
    Count_Eight = Text.count("8")
    Count_Nine = Text.count("9")
    
    Holes += Count_Zero
    Holes += Count_Four
    Holes += Count_Six
    Holes += Count_Eight
    Holes += Count_Eight
    Holes += Count_Nine
    
    Occurrences.append(Holes)
    VC += 1
  
  # Trimming Occurrences to Unique Values
  
  Occurrences = set(Occurrences)
  Occurrences = list(Occurrences)
  Occurrences = sorted(Occurrences)
  
  # Performing Sort
  
  Filtered = []
  Filtered.append("X")
  FL = len(Filtered)
  
  OC = 0
  OL = len(Occurrences)
  
  VC = 0
  VL = len(Values)
  
  while (FL <= VL) and (OC < OL):
    
    Target = Occurrences[OC]
    
    Item = Values[VC]
    Text = str(Values[VC])
    
    Holes = 0
    
    Count_Zero = Text.count("0")
    Count_Four = Text.count("4")
    Count_Six = Text.count("6")
    Count_Eight = Text.count("8")
    Count_Nine = Text.count("9")
    
    Holes += Count_Zero
    Holes += Count_Four
    Holes += Count_Six
    Holes += Count_Eight
    Holes += Count_Eight
    Holes += Count_Nine
    
    if (Holes == Target):
      Filtered.append(Item)
      VC += 1
    else:
      VC += 1
    
    if (VC == VL):
      VC = 0
      OC += 1
  
  # Establishing and Giving Answer
  Filtered = Filtered[1:]
  return Filtered

