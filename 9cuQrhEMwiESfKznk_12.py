"""


This is a companion to my [previous
challenge](https://edabit.com/challenge/mZqMnS3FsL2MPyFMg).

Given an English description of an integer in the range **0 to 999** , devise
a function that returns the integer in numeric form.

### Examples

    eng2nums("four") ➞  4
    
    eng2nums("forty") ➞ 40
    
    eng2nums("six hundred") ➞ 600
    
    eng2nums("one hundred fifteen") ➞ 115
    
    eng2nums("seven hundred sixty seven") ➞ 767

### Notes

  * No hyphens are used in test cases ("twenty three" not "twenty-three").
  * The word "and" is not used: "one hundred three" not "one hundred and three".

"""

ntoe = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
        40: "fourty", 50: "fifty", 60: "sixty", 70: "seventy",
        80: "eighty", 90: "ninety"}
eton = {v: k for k, v in ntoe.items()}
​
def eng2nums(s):
    if s in eton:
        return eton[s]
    n = 0
    if "hundred" in s:
        a, s = [_.strip() for _ in s.split("hundred")]
        n = 100 * eton[a]
    if s == "":
        return n
    if s in eton:
        return n + eton[s]
    a, b = s.split()
    n += eton[a] + eton[b]
    return n

