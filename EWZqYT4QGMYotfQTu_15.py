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

dic = {"a": (1,1), "b": (1,2), "c": (1,3), "d": (1,4), "e": (1,5), 
       "f": (2,1), "g": (2,2), "h": (2,3), "i": (2,4), "j": (2,5),
       "k": (1,3), 
       "l": (3,1), "m": (3,2), "n": (3,3), "o": (3,4), "p": (3,5),
       "q": (4,1), "r": (4,2), "s": (4,3), "t": (4,4), "u": (4,5),
       "v": (5,1), "w": (5,2), "x": (5,3), "y": (5,4), "z": (5,5)}
rdic = {v: k for k,v in dic.items()}
rdic[(1,3)] = "c"
​
def tap_code(text):
  if "." in text:
    ret = []
    words = text.split(" ")
    for i in range(len(words)//2):
      a, b = len(words[2*i]), len(words[2*i+1])
      ret.append(rdic[(a,b)])
    return "".join(ret)
  else:
    ret = []
    for c in text:
      a, b = dic[c]
      ret.append("."*a + " " + "."*b)
    return " ".join(ret)

