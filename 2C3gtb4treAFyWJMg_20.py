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
  text = text.lower()
  text = text.replace("j","i").replace("'","").replace(":","")
  letters = 'abcdefghiklmnopqrstuvwxyz'
  letter_dict = {}
  for i in range(len(letters)):
    letter_dict[letters[i]]=str((((i//5)+1)*10)+((i%5)+1))
  letter_dict.update({' ':' '})
  num_dict = {letter_dict[i]:i for i in letter_dict}
  del num_dict[' ']
  num_dict.update({'  ':' '})
  if (text[0] in letters) or (text[0]=='j'):
    return ''.join([letter_dict[i] for i in text])
  else:
    text = text.replace(' ','  ')
    text = [text[i:i+2] for i in range(0,len(text),2)]
    return ''.join([num_dict[i] for i in text])

