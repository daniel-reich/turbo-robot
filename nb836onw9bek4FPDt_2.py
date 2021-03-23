"""


Given a sentence, return the number of words which have the **same first and
last letter**.

### Examples

    count_same_ends("Pop! goes the balloon") ➞ 1
    
    count_same_ends("And the crowd goes wild!") ➞ 0
    
    count_same_ends("No I am not in a gang.") ➞ 1

### Notes

  * Don't count single character words (such as "I" and "A" in example #3).
  * The function should not be case sensitive, meaning a capital "P" should match with a lowercase one.
  * Mind the punctuation!
  * Bonus points indeed for using regex!

"""

def count_same_ends(st):
    import string
    pn = string.punctuation
    lst = []
    for a in st.split():
        s = ''
        for b in a:
            if not b in pn:
                s+=b.lower()
        lst.append(s)
    return sum((1 for a in lst if not len(a)==1 and a[0]==a[-1]))

