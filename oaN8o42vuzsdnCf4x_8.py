"""


Create a function that takes a list of words, scores the words based on the
Scrabble scoring table below, and returns a list of the highest scoring words.
The words on resulting list should be in the same relative order as the
original list.

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
  
### Examples

    best_words(["got", "test", "oh", "sat", "rents"]) ➞ ["oh", "rents"]
    
    best_words(["digest", "divest", "verge", "honey", "money"]) ➞ ["honey"]
    
    best_words(["berry", "whiz", "laughed", "ghetto", "psychic"]) ➞ ["whiz", "psychic"]

### Notes

Input and output should both be lists (see tests).

"""

def best_words(lst):
  letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 2, 
  3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
​
  arr, brr = [], []
  for x in lst:
    score = 0
    for c in x:
      score += points[letters.index(c.upper())]
    arr.append([score, x])
  for w in arr:
    if w[0] == max(arr)[0]:
      brr.append(w[1])
  return brr

