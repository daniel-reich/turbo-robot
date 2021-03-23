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

combintation = list()
a = [0, 3, 3, 3, 3, 3, 4, 3, 4]
def make_s(digits, string):
  if (len(string) == len(digits)):
    combintation.append(string)
  else:
    dc = int(digits[len(string)])
    f = 0
    for k in range(1,dc-1):
      f+=a[k]
​
    for i in range(f, f+a[dc-1]):
      make_s(digits,string+chr(97+i))
def letter_combinations(digits):
  combintation.clear()
  make_s(digits, "")
  print(combintation)
  return combintation

