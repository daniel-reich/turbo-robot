"""


In BlackJack, cards are counted with -1, 0, 1 values:

  * 2, 3, 4, 5, 6 are counted as +1
  * 7, 8, 9 are counted as 0
  * 10, J, Q, K, A are counted as -1

Create a function that counts the number and returns it from the list of cards
provided.

### Examples

    count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1
    
    count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6
    
    count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5

### Notes

  * String inputs will always be upper case.
  * You do not need to consider case sensitivity.
  * If the argument is empty, return `0`.
  * No input other than: `2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"`.

"""

def count(deck):
  result = []
  if deck == []:
    return 0
  else:
    for item in deck:
      if item in [2,3,4,5,6]:
        result.append(1)
      elif item in [7,8,9]:
        result.append(0)
      else:
        result.append(-1)
  ans = sum(result)
  return ans

