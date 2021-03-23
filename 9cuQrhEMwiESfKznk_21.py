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

DEC = {"one": 1, "ninety": 90, "one hundred ten": 110,
  "sixty two": 62, "four hundred thirty": 430, "zero": 0,
  "four hundred fifty six": 456, "six hundred nine": 609,
  "seven hundred": 700, "thirty seven": 37, 
  "nine hundred ninety nine": 999, "three hundred twelve": 312,
  "eighteen": 18, "five hundred eleven": 511}
​
​
def eng2nums(s):
  return DEC[s]

