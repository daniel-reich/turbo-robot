"""


The challenge is to recreate the functionality of the `title()` method into a
function called `emphasise()`. The `title()` method capitalises the first
letter of _every word_ and lowercases all of the other letters in the word.

### Examples

    emphasise("hello world") ➞ "Hello World"
    
    emphasise("GOOD MORNING") ➞ "Good Morning"
    
    emphasise("99 red balloons!") ➞ "99 Red Balloons!"

### Notes

  * You won't run into any issues when dealing with numbers in strings.
  * Please don't use the `title()` method directly :(

"""

def emphasise(txt): #long, time-waste method - but no in-built functions used at any point
  to_lower = {"A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f",
  "G": "g", "H": "h", "I": "i", "J": "j", "K": "k", "L": "l",
  "M": "m", "N": "n", "O": "o", "P": "p", "Q": "q", "R": "r",
  "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z"}
  new_txt = ""
  for i in txt:
    if i in to_lower:
      new_txt += to_lower[i]
    else:
      new_txt += i
  spl = []
  s = ""
  for i in new_txt:
    if i == ' ':
      spl += [s]
      s = ""
    else:
      s += i
  if s:
    spl += [s]
  to_upper = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
  'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
  'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R',
  's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
  'y': 'Y', 'z': 'Z'}
  spl, final = [to_upper[x[0]] + x[1:] if x[0] in to_upper else x for x in spl], ""
  for x in spl:
    final += x
    final += ' '
  return final[:-1]
  
def emphasise2(txt):
    return ' '.join(i.title() for i in txt.split())

