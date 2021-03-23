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

def tap_code(word):
​
  if not(isinstance(word,str)):
    print("You need to input a string")
    return FALSE
  elif "." in word:
    dots = word.split()
    out = []
    for letter in range(0,len(dots),2):
      row = (len(dots[letter])-1+13)*5
      col = len(dots[letter+1])-1
      ascii_val = row+col
      #if ascii_val == 67:
      # out.append("C/K")
      if ascii_val >= 75:
        out.append(str(chr(ascii_val+1)))
      else:
        out.append(str(chr(ascii_val)))
    separator = ''
    out = separator.join(out)
    out = out.lower()
​
  else:
    word = word.upper()
    print(word)
    out = []
    for letter in word:
      ascii_val = ord(letter)
      if ascii_val == 75:
        ascii_val = 67
      elif ascii_val > 75:
        ascii_val -= 1
      row = int(ascii_val/5)-13
      col = ascii_val % 5
      out.append((row+1)*".")
      out.append(" ")
      out.append((col+1)*".")
      out.append(" ")
    out.pop()
    separator = ''
    out = separator.join(out)
  return out

