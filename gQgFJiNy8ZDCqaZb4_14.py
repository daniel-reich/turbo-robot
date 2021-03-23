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
    s1l = [s1[i : ] for i in range(len(s1))]
    s2l = [s2[ : i] for i in range(1, len(s2) + 1)]
    x = list(set(s1l).intersection(set(s2l)))
    if x == []:
        return s1 + s2
    else:
        return s1 + s2[len(max(x)) : ]

