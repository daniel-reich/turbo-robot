"""


Tap code is a way to communicate messages via a series of taps (or knocks) for
each letter in the message. Letters are arranged in a 5x5 _polybius square_ ,
with the letter "K" being moved to the space with "C".

       1  2  3  4  5
    1  A  B C\K D  E
    2  F  G  H  I  J
    3  L  M  N  O  P
    4  Q  R  S  T  U
    5  V  W  X  Y  Z

Each letter is translated by tapping out the _row_ and _column_ number that
the letter appears in, leaving a short pause in-between. If we use "." for
each tap, and a single space to denote the pause:

    text = "break"
    
    "B" = (1, 2) = ". .."
    "R" = (4, 2) = ".... .."
    "E" = (1, 5) = ". ....."
    "A" = (1, 1) = ". ."
    "K" = (1, 3) = ". ..."

Another space is added between the groups of taps for each letter to give the
final code:

    "break" = ". .. .... .. . ..... . . . ..."

Write a function that returns the tap code if given a word, or returns the
translated word (in lower case) if given the tap code.

### Examples

    tap_code("break") ➞ ". .. .... .. . ..... . . . ..."
    
    tap_code(".... ... ... ..... . ..... ... ... .... ....") ➞ "spent"

### Notes

For more information on tap code, please see the resources section. The code
was widely used in WW2 as a way for prisoners to communicate.

"""

import re
​
dictio = {'11': 'a', '12': 'b', '13': 'c', '14': 'd', '15': 'e',
        '21': 'f', '22': 'g', '23': 'h', '24': 'i', '25': 'j', 
        '31': 'l', '32': 'm', '33': 'n', '34': 'o', '35': 'p',
        '41': 'q', '42': 'r', '43': 's', '44': 't', '45': 'u',
        '51': 'v', '52': 'w', '53': 'x', '54': 'y', '55': 'z'}
        
def dot_to_str(dots):
  pattern = '\.+\s{1}\.+'
  matches = re.findall(pattern, dots)
  res = ''
  for match in matches:
    num1, num2 = match.split()
    res += dictio[str(len(num1)) + str(len(num2))]
  return res
  
def str_to_dot(string):
  li = list(string)
  res = []
  for letter in string:
    if letter == 'k': 
      res.append('. ...')
      continue
    numDots = list(dictio.keys())[list(dictio.values()).index(letter)]
    res.append('.' * int(numDots[0]))
    res.append('.' * int(numDots[1]))
  return ' '.join(res)
  
def tap_code(text):
  if set(text) == {'.', ' '}: return dot_to_str(text)
  else: return str_to_dot(text)

