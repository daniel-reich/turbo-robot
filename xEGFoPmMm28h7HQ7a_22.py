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

from itertools import product
def letter_combinations(digits):
  dict = {
  "1" : [],
  "2" : ["a","b","c"],
  "3" : ["d","e","f"],
  "4" : ["g","h","i"],
  "5" : ["j","k","l"],
  "6" : ["m","n","o"],
  "7" : ["p","q","r","s"],
  "8" : ["t","u","v"],
  "9" : ["w","x","y","z"]}
  
  lst =  [dict[digit] for digit in digits]
  p = lst[0]
  for i, q in enumerate(lst[1:]):
    p = ["".join(r) for r in product(p,q)]
  return p

