"""


Create a function that takes a string and censors words **over four
characters** with `*`.

### Examples

    censor("The code is fourty") ➞ "The code is ******"
    
    censor("Two plus three is five") ➞ "Two plus ***** is five"
    
    censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"

### Notes

  * Don't censor words with exactly four characters.
  * If all words have four characters or less, return the original string.
  * The amount of `*` is the same as the length of the word.

"""

def censor(s):
  words = s.split(" ")
  word = ""
  for y,x in enumerate(words):
    if(len(x) > 4):
       for i in x:
          word = word + "*"
       words[y] = word
       word = ""
  return " ".join(words)

