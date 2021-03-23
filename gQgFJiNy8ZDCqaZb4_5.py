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

def checkoverlap(s1l, s2l):
    for i in range(0,len(s1l)):
        try:
            if s1l[i]!=s2l[i]:
                return False
        except IndexError:
            return False
    return True
​
    
​
def overlap(s1, s2):
    s1l=list(s1)
    s2l=list(s2)
    for i in range(0,len(s1)):
        if s1l[i]==s2l[0]:
            if (checkoverlap(s1l[i:],s2l)):
                return ''.join(s1l[:i])+s2
    return s1+s2

