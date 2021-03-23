"""


Julius Caesar protected his confidential information by encrypting it using a
cipher. Caesar's cipher (check **Resources** tab for more info) shifts each
letter by a number of letters. If the shift takes you past the end of the
alphabet, just rotate back to the front of the alphabet. In the case of a
rotation by `3`, _w, x, y_ and _z_ would map to _z, a, b_ and _c_.

Create a function that takes a string `s` (text to be encrypted) and an
integer `k` (the rotation factor). It should return an encrypted string.

### Examples

    caesar_cipher("middle-Outz", 2) ➞ "okffng-Qwvb"
    
    # m -> o
    # i -> k
    # d -> f
    # d -> f
    # l -> n
    # e -> g
    # -    -
    # O -> Q
    # u -> w
    # t -> v
    # z -> b
    
    caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 5)
    ➞ "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"
    
    caesar_cipher("A friend in need is a friend indeed", 20)
    ➞ "U zlcyhx ch hyyx cm u zlcyhx chxyyx"

### Notes

All test input will be a valid ASCII string.

"""

def caesar_cipher(s, k):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  length = 25
  cypher = ""
  yup = False
  
  
  for ch in s:
    if(not ch.isalpha()):
      cypher += ch
      continue
      
    if(ch.isupper()):
      yup = True
    
    current_index = alpha.find(ch.lower())
    
    for i in range(k,0,-1):
      if(current_index == 25):
        current_index = 0
      else:
        current_index += 1
    new_index = current_index
    
    nxt = alpha[new_index]
    if(yup):
      cypher += nxt.upper()
      yup = False
    else:
      cypher += nxt
  return cypher
