"""


The **Polybius Square** cipher is a simple substitution cipher that makes use
of a 5x5 square grid. The letters A-Z are written into the grid, with "I" and
"J" typically sharing a slot (as there are 26 letters and only 25 slots).

| 1| 2| 3| 4| 5  
---|---|---|---|---|---  
 **1**|  A| B| C| D| E  
 **2**|  F| G| H| I/J| K  
 **3**|  L| M| N| O| P  
 **4**|  Q| R| S| T| U  
 **5**|  V| W| X| Y| Z  
  
To encipher a message, each letter is merely replaced by its row and column
numbers in the grid.

Create a function that takes a plaintext or ciphertext message, and returns
the corresponding ciphertext or plaintext.

### Examples

    polybius("Hi") ➞ "2324"
    
    polybius("2324  4423154215") ➞ "hi there"
    
    polybius("543445 14343344 522433 21422415331443 52244423 4311311114") ➞ "you dont win friends with salad"

### Notes

  * As "I" and "J" share a slot, both are enciphered into 24, but deciphered only into "I" (see third and fourth test).
  * Any charactor other than letters and spaces should be dropped from the cypher.

"""

def polybius(text):
  if str.isdigit(text[0]):
    return decode(text)
  return encode(text)
​
def encode(text):
  encode_dict = {
    "A": "11", "B": "12", "C": "13", "D": "14", "E": "15", 
    "F": "21", "G": "22", "H": "23", "I": "24", "J": "24", "K": "25",
    "L": "31", "M": "32", "N": "33", "O": "34", "P": "35",
    "Q": "41", "R": "42", "S": "43", "T": "44", "U": "45",
    "V": "51", "W": "52", "X": "53", "Y": "54", "Z": "55", " ": " "
  }
  
  s = ""
  for char in str.upper(text):
    if char in encode_dict:
      s += str.lower(str(encode_dict.get(char)))
    
  return s
​
def decode(text):
  decode_dict = {
    "11": "A", "12": "B", "13": "C", "14": "D", "15": "E", 
    "21": "F", "22": "G", "23": "H", "24": "I", "25": "K",
    "31": "L", "32": "M", "33": "N", "34": "O", "35": "P",
    "41": "Q", "42": "R", "43": "S", "44": "T", "45": "U",
    "51": "V", "52": "W", "53": "X", "54": "Y", "55": "Z" 
  }
  
  s = ""
  i = 0
  while i < len(text) - 1:
    if text[i] == ' ':
      s += ' '
      i += 1
    else:
      temp = text[i] + text[i+1]
      if temp in decode_dict:
        s += str.lower(str(decode_dict.get(temp)))
        i += 2
  return s

