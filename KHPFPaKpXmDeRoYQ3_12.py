"""


Write a function that takes a list of lists and returns the value of all of
the symbols in it, where each symbol adds or takes something from the total
score. Symbol values:

  * `#` = 5
  * `O` = 3
  * `X` = 1
  * `!` = -1
  * `!!` = -3
  * `!!!` = -5

A list of lists containing 2 `#`s, a `O`, and a `!!!` would equal (0 + 5 + 5 +
3 - 5) 8.

If the final score is negative, return `0` (e.g. 3 `#`s, 3 `!!`s, 2 `!!!`s and
a `X` would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return `0`.

### Examples

    check_score([
      ["#", "!"],
      ["!!", "X"]
    ]) ➞ 2
    
    check_score([
      ["!!!", "O", "!"],
      ["X", "#", "!!!"],
      ["!!", "X", "O"]
    ]) ➞ 0
    
    check_score([
      ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
      ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
      ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
      ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
      ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
      ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
      ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
      ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
      ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
      ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
      ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
      ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
      ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
      ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
    ]) ➞ 12

### Notes

Strings in the lists will only be `#`, `O`, `X`, `!`, `!!` and `!!!`.

"""

def check_score(s):
  myDict = {'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
  myScore = 0
  for a in range(len(s)):
    for b in range(len(s[a])):
      myScore += myDict[s[a][b]]
  if myScore < 0:
    return 0
  return myScore
