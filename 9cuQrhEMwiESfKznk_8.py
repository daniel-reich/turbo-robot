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

def eng2nums(s):
  
  Text = str(s)
  Words = Text.split()
  Length = len(Words)
​
  Total = 0
​
  ############################################################
  #   HUNDREDS COLUMN
  ############################################################
​
  if (Length > 1) and (Words[0] == "one") and (Words[1] == "hundred"):
    Total += 100
​
  if (Length > 1) and (Words[0] == "two") and (Words[1] == "hundred"):
    Total += 200
​
  if (Length > 1) and (Words[0] == "three") and (Words[1] == "hundred"):
    Total += 300
​
  if (Length > 1) and (Words[0] == "four") and (Words[1] == "hundred"):
    Total += 400
​
  if (Length > 1) and (Words[0] == "five") and (Words[1] == "hundred"):
    Total += 500
​
  if (Length > 1) and (Words[0] == "six") and (Words[1] == "hundred"):
    Total += 600
​
  if (Length > 1) and (Words[0] == "seven") and (Words[1] == "hundred"):
    Total += 700
​
  if (Length > 1) and (Words[0] == "eight") and (Words[1] == "hundred"):
    Total += 800
​
  if (Length > 1) and (Words[0] == "nine") and (Words[1] == "hundred"):
    Total += 900
​
  ############################################################
  #   TENS COLUMN
  ############################################################
​
  if ("ten" in Words):
    Total += 10
​
  if ("eleven" in Words):
    Total += 11
​
  if ("twelve" in Words):
    Total += 12
​
  if ("thirteen" in Words):
    Total += 13
​
  if ("fourteen" in Words):
    Total += 14
​
  if ("fifteen" in Words):
    Total += 15
​
  if ("sixteen" in Words):
    Total += 16
​
  if ("seventeen" in Words):
    Total += 17
​
  if ("eighteen" in Words):
    Total += 18
​
  if ("nineteen" in Words):
    Total += 19
​
  if ("twenty" in Words):
    Total += 20
​
  if ("thirty" in Words):
    Total += 30
​
  if ("forty" in Words):
    Total += 40
​
  if ("fifty" in Words):
    Total += 50
​
  if ("sixty" in Words):
    Total += 60
​
  if ("seventy" in Words):
    Total += 70
​
  if ("eighty" in Words):
    Total += 80
​
  if ("ninety" in Words):
    Total += 90
​
  ############################################################
  #   UNITS COLUMN OF LIST LENGTH OF ONE
  ############################################################
​
  if (Length == 1) and (Words[0] == "one"):
    Total += 1
​
  if (Length == 1) and (Words[0] == "two"):
    Total += 2
​
  if (Length == 1) and (Words[0] == "three"):
    Total += 3
​
  if (Length == 1) and (Words[0] == "four"):
    Total += 4
​
  if (Length == 1) and (Words[0] == "five"):
    Total += 5
​
  if (Length == 1) and (Words[0] == "six"):
    Total += 6
​
  if (Length == 1) and (Words[0] == "seven"):
    Total += 7
​
  if (Length == 1) and (Words[0] == "eight"):
    Total += 8
​
  if (Length == 1) and (Words[0] == "nine"):
    Total += 9
​
  ############################################################
  #   UNITS COLUMN OF LIST LENGTH OF TWO
  ############################################################
​
  if (Length == 2) and (Words[1] == "one"):
    Total += 1
​
  if (Length == 2) and (Words[1] == "two"):
    Total += 2
​
  if (Length == 2) and (Words[1] == "three"):
    Total += 3
​
  if (Length == 2) and (Words[1] == "four"):
    Total += 4
​
  if (Length == 2) and (Words[1] == "five"):
    Total += 5
​
  if (Length == 2) and (Words[1] == "six"):
    Total += 6
​
  if (Length == 2) and (Words[1] == "seven"):
    Total += 7
​
  if (Length == 2) and (Words[1] == "eight"):
    Total += 8
​
  if (Length == 2) and (Words[1] == "nine"):
    Total += 9
​
  ############################################################
  #   UNITS COLUMN OF LIST LENGTH OF THREE
  ############################################################
​
  if (Length == 3) and (Words[2] == "one"):
    Total += 1
​
  if (Length == 3) and (Words[2] == "two"):
    Total += 2
​
  if (Length == 3) and (Words[2] == "three"):
    Total += 3
​
  if (Length == 3) and (Words[2] == "four"):
    Total += 4
​
  if (Length == 3) and (Words[2] == "five"):
    Total += 5
​
  if (Length == 3) and (Words[2] == "six"):
    Total += 6
​
  if (Length == 3) and (Words[2] == "seven"):
    Total += 7
​
  if (Length == 3) and (Words[2] == "eight"):
    Total += 8
​
  if (Length == 3) and (Words[2] == "nine"):
    Total += 9
​
  ############################################################
  #   UNITS COLUMN OF LIST LENGTH OF FOUR
  ############################################################
​
  if (Length == 4) and (Words[3] == "one"):
    Total += 1
​
  if (Length == 4) and (Words[3] == "two"):
    Total += 2
​
  if (Length == 4) and (Words[3] == "three"):
    Total += 3
​
  if (Length == 4) and (Words[3] == "four"):
    Total += 4
​
  if (Length == 4) and (Words[3] == "five"):
    Total += 5
​
  if (Length == 4) and (Words[3] == "six"):
    Total += 6
​
  if (Length == 4) and (Words[3] == "seven"):
    Total += 7
​
  if (Length == 4) and (Words[3] == "eight"):
    Total += 8
​
  if (Length == 4) and (Words[3] == "nine"):
    Total += 9
​
  ############################################################
  #   GIVING ANSWER
  ############################################################
  return Total

