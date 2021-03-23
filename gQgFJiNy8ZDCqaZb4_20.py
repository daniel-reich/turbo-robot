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
  if s1 == s2:
    return s1
​
  current = 1
  cond = True
  j = 0
  for i in range(len(s1), 0, -1):
    if s1[i-1:] == s2[:j+1]:
      current = i
      cond = False
    j += 1   
​
  if cond == True:
    return s1 + s2
  return s1[:current-1] + s2

