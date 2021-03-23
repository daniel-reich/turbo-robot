"""


Given a string containing digits from `2-9` inclusive, return all possible
letter combinations that the number could represent. A mapping of digit to
letters (just like on the telephone buttons) is given below. Note that 1 does
not map to any letters.

![Alternative Text](https://edabit-challenges.s3.amazonaws.com/200px-
Telephone-keypad2.svg.png)

### Examples

    letter_combinations("23") ➞ ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    
    letter_combinations("532") ➞ ["jda", "jdb", "jdc", "jea", "jeb", "jec", "jfa", "jfb", "jfc", "kda", "kdb", "kdc", "kea", "keb", "kec", "kfa", "kfb", "kfc", "lda", "ldb", "ldc", "lea", "leb", "lec", "lfa", "lfb", "lfc"]

### Notes

N/A

"""

from itertools import combinations
​
def letter_combinations (nums) :
  # my code is not very good
    '''input : a string of numbers
    output : all the letters possibly written with these numbers on a phone'''
    eq = {'2': list('abc'), '3': list('def'), '4':list('ghi'), '5': list('jkl'), '6': list('mno'), \
          '7': list('pqrs'), '8': list('tuv'), '9': list('wxyz')}
    possible = []
    for i in nums :
        for j in eq[i] :
            possible.append (j)
    sol = [''.join(i) for i in combinations (possible, len(nums)) if len(i) % len(nums) == 0]
    res = []
    banned = []
    for i in sol :
        for j in range (len(i)) :
            if i[j] in eq[nums[j]] :
                res.append (i)
            else :
                banned.append (i)
    return sorted(list(set([i for i in res if i not in banned])))

