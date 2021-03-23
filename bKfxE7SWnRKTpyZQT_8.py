"""


Create a function that takes a string and replaces the vowels with another
character.

  * a = 1
  * e = 2
  * i = 3
  * o = 4
  * u = 5

### Examples

    replace_vowel("karachi") ➞ "k1r1ch3"
    
    replace_vowel("chembur") ➞ "ch2mb5r"
    
    replace_vowel("khandbari") ➞ "kh1ndb1ri"

### Notes

The input will always be in lowercase.

"""

def replace_vowel(word):
  
  Step01 = str(word)
  Step02 = Step01.replace("a","1")
  Step03 = Step02.replace("e","2")
  Step04 = Step03.replace("i","3")
  Step05 = Step04.replace("o","4")
  Step06 = Step05.replace("u","5")
  Answer = Step06
  
  return Answer

