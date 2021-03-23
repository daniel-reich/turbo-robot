"""


Given two words, overlap them in such a way, morphing the last few letters of
the first word with the first few letters of the second word. Return the
shortest overlapped word possible.

### Examples

    overlap("sweden", "denmark") ➞ "swedenmark"
    
    overlap("edabit", "iterate") ➞ "edabiterate"
    
    overlap("honey", "milk") ➞ "honeymilk"
    
    overlap("dodge", "dodge") ➞ "dodge"

### Notes

  * All words will be given in lowercase.
  * If no overlap is possible, return both words one after the other (example #3).

"""

def overlap(s1, s2):
  trim = []
  if s1 == s2:
    return s1
  for i in range(len(s2)):
    trim.append(s2[i])
    if ''.join(trim) not in s1 or i == len(s2) - 1:
      if ''.join(trim[:-1]) != s1[-(len(trim) - 1):]:
        return s1+s2
      return s1 + s2[i:]

