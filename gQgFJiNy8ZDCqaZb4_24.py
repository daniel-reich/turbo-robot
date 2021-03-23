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
    elif len(set(list(s1)).intersection(set(list(s2)))) == 0:
        return s1 + s2
    else:
        new = ""
        for i in range(len(s1)):
            if s1[i] == s2[0]:
                new += s1[:i]
                s2 = s2.replace(s1[i:],"")
                new += s1[i:]
                new += s2
                break
​
        return new

