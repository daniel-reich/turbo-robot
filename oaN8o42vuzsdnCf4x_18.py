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
  score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 2, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
  def scoreWord(word):
    return sum([score[i.lower()] for i in word])
    
  highest = 0
  for i in range(len(lst)):
    if scoreWord(lst[i]) > highest: highest = scoreWord(lst[i])
    
  return [w for w in lst if scoreWord(w) == highest]

