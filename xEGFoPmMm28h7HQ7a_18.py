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

def letter_combinations(digits):
  phonelist=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
  combinations=[]
  try:
    firstnumber=phonelist[int(digits[0])-2]
    secondnumber=phonelist[int(digits[1])-2]
    thirdnumber=phonelist[int(digits[2])-2]
    for i in range(0,len(firstnumber)):
      for j in range (0,len(secondnumber)):
        for k in range (0,len(thirdnumber)):
          combinations.append("{}{}{}".format(firstnumber[i],secondnumber[j],thirdnumber[k]))
    return combinations
  except:
    firstnumber=phonelist[int(digits[0])-2]
    secondnumber=phonelist[int(digits[1])-2]
    for i in range(0,len(firstnumber)):
      for j in range (0,len(secondnumber)):
          combinations.append("{}{}".format(firstnumber[i],secondnumber[j]))
    return combinations

