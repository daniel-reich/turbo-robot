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
  n1,n2=len(s1),len(s2)
  n = min(n1,n2)
  for i in range(n+1):
    if s1[-n+i:] == s2[:n-i]:
      return s1+s2[n-i:]
  return s1+s2

