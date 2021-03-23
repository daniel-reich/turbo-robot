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

def tap_code(text):
  l=[
  ["a","b","c\k","d","e"],
  ["f","g","h","i","j"],
  ["l","m","n","o","p"],
  ["q","r","s","t","u"],
  ["v","w","x","y","z"],
  ]
​
  final=[]
  temp=[]
  if text.isalpha():
    for k in text:
      for i in range(len(l)): 
        for j in range(len(l[i])):
          if l[i][j] is k:
            s="."*(i+1)+" "*1+"."*(j+1)
            temp.append(s)
      if k is "c" or k is "k":
        temp.append(". ...")
                
    final.append(" ".join(temp))
    temp.clear()
    return final[0]
  else:
    r=text.split()
    row=[r[i].count(".")-1 for i in range(0,len(r),2)]
    col=[r[i].count(".")-1 for i in range(1,len(r),2)]
    for r,c in zip(row,col) :
      if l[r][c] is "c\k":
        temp.append("c")
      else:
        temp.append(l[r][c])
    final.append("".join(temp))
    return final[0]

