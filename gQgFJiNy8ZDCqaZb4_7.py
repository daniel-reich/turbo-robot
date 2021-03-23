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
  res=""
  l=1
  for i in range(len(s1)):
      if s1[i]==s2[0]:
          l=len(s1)-i
          break   
  if s1[i:]==s2[:l]:
      res+=s1+s2[l:]
  elif s1==s2:
      res+=s1
  else:
      res+=s1+s2
  return res

