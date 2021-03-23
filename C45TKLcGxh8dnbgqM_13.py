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
  lowAlph = list("abcdefghijklmnopqrstuvwxyz")
  highAlph = list("abcdefghijklmnopqrstuvwxyz".upper())
  getInd = {}
  for i, c in enumerate(lowAlph):
    getInd[c] = i
  ret = ""
  for i in s:
    if i.islower():
      ind = getInd[i]
      ind = (ind+k)%26
      ret += lowAlph[ind]
    elif i.isupper():
      ind = getInd[i.lower()]
      ind = (ind+k)%26
      ret += highAlph[ind]
    else:
      ret += i
  return ret

