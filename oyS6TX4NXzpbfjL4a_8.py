"""


This challenge is based on the game Scrabble. Each word you play is scored
based on the point value of each tile/letter (see first table), as well as
additional points conferred by any special squares your tiles land on (see
second table).

Create a function that takes a list representing a row of squares in a
Scrabble board, and a string representing the word to be played. The list will
consist of `-` representing normal squares, and "DL", "TL", "DW" representing
special squares. Return the index of the list where the first letter of the
word should be placed to maximise the score of the word to be played. Return
the lowest index, if several exist.

Letter| Points  
---|---  
A| 1  
B| 3  
C| 3  
D| 2  
E| 1  
F| 4  
G| 2  
H| 4  
I| 1  
J| 8  
K| 5  
L| 2  
M| 3  
N| 1  
O| 1  
P| 3  
Q| 10  
R| 1  
S| 1  
T| 1  
U| 1  
V| 4  
W| 4  
X| 8  
Y| 4  
Z| 10  
Special Square| Meaning  
---|---  
DL| Double letter score - doubles the point value of a letter placed on the
square  
TL| Triple letter score - triples the point value of a letter placed on the
square  
DW| Double word score - doubles the score of an entire word if one of its
letters is placed on the square  
  
### Examples

    best_start(["-","DW","-","-","-","TL","-","-","-","TL","-","-","-","DW","-"], "quiz") ➞ 0
    # Doubling the entire word maximises the score. Starting at
    # indices 1,10, and 11 have the same effect, but the function
    # should return the lowest index.
    
    best_start(["-","DW","-","-","-","TL","-","-","-","TL","-","-","-","DW","-"], "quit") ➞ 5
    # Tripling the first letter alone gives a higher score than
    # doubling the entire word, as the other 3 letters have
    # low point-values.
    
    best_start(["-","DW","-","-","-","TL","-","-","-","TL","-","-","-","DW","-"], "quart") ➞ 9
    # Tripling the first (high-scoring) letter, and doubling the word.
    
    best_start(["-","DW","-","-","-","TL","-","-","-","TL","-","-","-","DW","-"], "quartz") ➞ 0
    # Tripling the last (high-scoring) letter, and doubling the word.
    # Index 9 has the same effect (tripling the first letter, doubling
    # the word), but 0 is the lower index.

### Notes

N/A

"""

def best_start(lst, word):
  letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 2, 
  3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
  
  arr = []
  for x in word:
    score = 0
    for c in x:
      score += points[letters.index(c.upper())]
    arr.append(score)
    
  DW = sum(arr)*2       # Double word score
  TL = max(arr)*2 + sum(arr)  # Triple letter score
  DTL = max(arr)*2 + (arr[arr.index(max(arr))]+ 4)*2  # Double Triple letter score
  
  if len(word) <= 4:
    #we can only hit one special square
    if DW > TL:
      index = lst.index("DW") #can index get lower?
      while lst[index] == "DW" or lst[index] == '-':
        if index > 0:
          index -= 1
        else : break
      return index
    else : 
      if arr.index(max(arr)) == 0:
        return lst.index("TL")
      else : return lst.index("TL") - arr.index(max(arr))
      
  elif len(word) > 4 and len(word) <= 8:
    #we will utilize TL and DW
    if arr.count(max(arr)) == 1:
      if arr.index(max(arr)) == 0:
        for i in range(len(lst)-1, -1, -1):
          if lst[i] == "TL":
            return i
    else :
      #we will utlize DW and TL
      index = lst.index("DW") #can index get lower?
      while lst[index] == "DW" or lst[index] == '-':
        if index > 0:
          index -= 1
        else : break
      return index

