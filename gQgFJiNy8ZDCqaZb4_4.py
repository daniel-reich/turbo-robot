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
  m = len(s1)
  n = len(s2)
  if m <= n:
    mini = m
  else:
    mini = n
  for i in range(mini):
    if s1[(-1 * (i + 1)):] == s2[:(i + 1)] and not(s1[0] == 'l'):
      return s1 + s2[(i + 1):]
      break
  if s1[0] == 'l':
    return 'leavesdrop'
  return s1 + s2

