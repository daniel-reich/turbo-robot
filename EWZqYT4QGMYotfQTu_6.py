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

def read(t,R):
  a = []
  r = 0
  codes = [[1,1],[1,2],[1,3],[1,4],[1,5],[2,1],[2,2],[2,3],[2,4],[2,5],[3,1],[3,2],[3,3],[3,4],[3,5],[4,1],[4,2],[4,3],[4,4],[4,5],[5,1],[5,2],[5,3],[5,4],[5,5]]
  letters = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  if t == 0:
    for l in codes:
      if R == l:
        return letters[codes.index(l)]
  if t == 1:
    for l in R:
      if l == 'k':
        l = 'c'
      r += 1
      if r == len(R):
        a.append(('.' * codes[letters.index(l)][0]) + " "  + "." * (codes[letters.index(l)][1]))
      else:
        a.append(('.' * codes[letters.index(l)][0]) + " "  + "." * (codes[letters.index(l)][1])+" ")
  return ''.join(a)
      
def tap_code(text):
  rc = 0
  r = 0
  c = 0
  p = 0
  pc = 0
  a = []
  if "."in text:
    for d in text:
      pc += 1
      if d == '.':
        if p % 2 == 0:
          r += 1
        else:
          c+=1
      if d == ' ' or  (pc + 1) > len(text):
        p+=1
      if (p%2 == 0 and p>0):
        a.append(read(0,[r,c]))
        p = 0
        r = 0
        c = 0
  else:
    return read(1,text)
  return ''.join(a)

