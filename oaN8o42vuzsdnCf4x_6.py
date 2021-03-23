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
  m = max([score(word) for word in lst])
  return [word for word in lst if score(word) == m]
def score(word):
  keys = [chr(i) for i in range(97, 123)]
  vals = '13321424185231130111144840'
  dic = {k: (10 if v == '0' else int(v)) for k, v in zip(keys, vals)}
  return sum([dic[k] for k in word])

