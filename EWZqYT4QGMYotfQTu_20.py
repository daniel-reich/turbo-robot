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

def tap_code(n):
  if("." not in n): 
    a=[["a","b","ck","d","e"],["f","g","h","i","j"],["l","m","n","o","p"],["q","r","s","t","u"],["v","w","x","y","z"]]  
    ans=''
    for i in n:
      row=0
      col=0
      if(i=="c" or i=="k"):
        row=0
        col=2
      else:
        while(row<5):
          check=0
          col=0
          while(col<5):
            if(a[row][col]==i):
              check=1
              
              break
            col+=1
          if(check==1):
            break
          row+=1
​
      row+=1
      col+=1
      aa="."*row+" "
      bb="."*col+" "
      ans+=(aa+bb)
    return ans[0:len(ans)-1]  
  else:
    a=[["a","b","c","d","e"],["f","g","h","i","j"],["l","m","n","o","p"],["q","r","s","t","u"],["v","w","x","y","z"]]
    n=n.split(" ")
    i=list()
    j=list()
    for x in range(0,len(n),2):
      i.append(len(n[x])-1)
    for x in range(1,len(n),2):
      j.append(len(n[x])-1)
    ans=''
    for x in range(0,len(i)):
      ans+=a[i[x]][j[x]]
    return ans

