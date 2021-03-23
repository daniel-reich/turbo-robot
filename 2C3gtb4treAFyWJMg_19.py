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
  alp = "abcdefghiklmnopqrstuvwxyz"
  num = "12345"
  result = ""
  is_num = bool(text.strip()[0] in num)
  
  if is_num:
    i = 0
    while i < len(text):
      if text[i] == " ":
        result += " "
        i += 1
      else:
        result += alp[(5*(int(text[i])-1))+int(text[i+1])-1]
        i += 2
  else:
    text = text.lower()
    text = text.replace("j","i")
    for i in range(0,len(text)):
      if text[i] == " ":
        result += " "
      elif text[i] in alp:
        result += str(int((alp.index(text[i])//5)+1)) + str(int((alp.index(text[i]) % 5) + 1)) 
  return result

