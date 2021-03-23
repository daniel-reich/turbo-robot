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

def create_letter_dict():
  d = dict()
  alphabet = "abcdefghiklmnopqrstuvwxyz"
  for i in range(5):
    for j in range(5):
      d[alphabet[5*i + j]] = str(i+1) + str(j+1)  
    
  d['j'] = '24'
  return d
​
def create_number_dict():
  d = dict()
  alphabet = "abcdefghiklmnopqrstuvwxyz"
  for i in range(5):
    for j in range(5):
      d[str(i+1) + str(j+1)] = alphabet[5*i + j]
​
  return d
​
def encode(txt):
  letter_dict = create_letter_dict()
  encoded = ""
  for letter in txt:
    encoded += letter_dict[letter.lower()]
​
  return encoded
​
def decode(txt):
  number_dict = create_number_dict()
  decoded = ""
  for i in range(len(txt)):
    if i % 2 == 0:
      decoded += number_dict[txt[i] + txt[i+1]]
​
  return decoded
​
def polybius(text):
  words_list = text.split(" ")
  final_txt = list()
  #if want to decode
  if words_list[0] <= "9" and words_list[0] >= "0":
    for word in words_list:
      final_txt.append(decode(word))
​
  #want to encode
  else:
    for word in words_list:
      final_txt.append(encode(word))
​
  return ' '.join(final_txt)
def create_letter_dict():
  d = dict()
  alphabet = "abcdefghiklmnopqrstuvwxyz"
  for i in range(5):
    for j in range(5):
      d[alphabet[5*i + j]] = str(i+1) + str(j+1)  
    
  d['j'] = '24'
  return d
​
def create_number_dict():
  d = dict()
  alphabet = "abcdefghiklmnopqrstuvwxyz"
  for i in range(5):
    for j in range(5):
      d[str(i+1) + str(j+1)] = alphabet[5*i + j]
​
  return d
​
def encode(txt):
  letter_dict = create_letter_dict()
  encoded = ""
  for letter in txt:
    encoded += letter_dict[letter.lower()]
​
  return encoded
​
def decode(txt):
  number_dict = create_number_dict()
  decoded = ""
  for i in range(len(txt)):
    if i % 2 == 0:
      decoded += number_dict[txt[i] + txt[i+1]]
​
  return decoded
​
def polybius(text):
  not_allowed = ["'", ".", "?", ":"]
  text = ''.join([i for i in text if i not in not_allowed])
  words_list = text.split(" ")
  final_txt = list()
  #if want to decode
  if words_list[0] <= "9" and words_list[0] >= "0":
    for word in words_list:
      final_txt.append(decode(word))
​
  #want to encode
  else:
    for word in words_list:
      final_txt.append(encode(word))
​
  return ' '.join(final_txt)

