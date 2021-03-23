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
  smaller = min([len(s1),len(s2)])
  if s1 == s2:
    return s1
  if s1 in s2: 
    return s2
  for i in range(smaller): 
    backthrough = smaller - i - 1
    revthrough = (-1 * backthrough)
    print(backthrough)
    print(revthrough)
    print(s1[revthrough:])
    print(s2[0:backthrough])
    print('-----')
    if s1[revthrough:] == s2[0:backthrough]: 
      begin = s1[0:revthrough]
      end = s2[backthrough:]
      overlap = s1[revthrough:]
      return begin + overlap + end
  return s1+s2

