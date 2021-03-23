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
  letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  Caps =  ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  new = ""
  for x in s:
    count = 0
    i = 1
    if x.upper() != x:
      for y in range(0,len(letters)):
        if letters[y] == x:
          if y+k >= len(letters):
            while (y+k)- (i*len(letters)) >= len(letters):
              i +=1
            new += letters[(y+k)-(i*len(letters))]
            count += 1
            break
          else:
            new += letters[(y+k)]
            count += 1
            break
    if x.upper() == x:
      for y in range(0,len(letters)):
        if Caps[y] == x:
          if y+k >= len(letters):
            while (y+k)- (i*len(letters)) >= len(letters):
              i +=1
            new += Caps[y+k-(i*len(letters))]
            count += 1
            break
          else:
            new += Caps[y+k]
            count += 1
            break
    if count == 0:
      new += x
  return new

