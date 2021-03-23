"""


Create a function that takes a string and returns the first character of every
word if the length of the word is even and the middle character if the length
of the word is odd.

### Examples

    stmid("Alexa have to paid") ➞ "ehtp"
    # "e" is the middle character of "Alexa"
    # "h" is the first character of "have"
    
    stmid("Th3 0n3 4nd 0n1y") ➞ "hnn0"
    
    stmid("who is the winner") ➞ "hihw"

### Notes

N/A

"""

def middle(word):
  if len(word) == 1:
    return word
  return middle(word[1:-1])
​
def stmid(string):
  words = string.split(' ')
  output = ''
  for word in words:
    if len(word) % 2 == 0:
      output += word[0]
    else:
      output += middle(word)
  return output

