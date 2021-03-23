"""


Create a function that, given a phrase and a number of letters guessed,
returns a string with hyphens `-` for every letter of the phrase not guessed,
and each letter guessed in place.

### Examples

    hangman("helicopter", ["o", "e", "s"]) ➞ "-e---o--e-"
    
    hangman("tree", ["r", "t", "e"]) ➞ "tree"
    
    hangman("Python rules", ["a", "n", "p", "r", "z"]) ➞ "P----n r----"
    
    hangman("He"s a very naughty boy!", ["e", "a", "y"]) ➞ "-e"- a -e-y -a----y --y!"

### Notes

  * The letters are always given in lowercase, but they should be returned in the same case as in the original phrase (see example #3).
  * All characters other than letters should always be returned (see example #4).

"""

def hangman(phrase, lst):
  
  Status = ""
  CODE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  Counter = 0
  Length = len(phrase)
  
  while (Counter < Length):
  
    Item = phrase[Counter]
    
    if (Item.upper() in lst) or (Item.lower() in lst):
      Status = Status + Item
      Counter += 1
    elif (Item.upper() not in CODE):
      Status = Status + Item
      Counter += 1
    else:
      Status = Status + "-"
      Counter += 1
  
  return Status

