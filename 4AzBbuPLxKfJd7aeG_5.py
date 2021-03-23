"""


Create a function that takes an encryption key (a string with an even number
of characters) and a message to encrypt. Group the letters of the key by two:

    "gaderypoluki" -> "ga de ry po lu ki"

Now take the message for encryption. If the message character appears in the
key, replace it with an adjacent character in the grouped version of the key.
If the message character does not appear in the key, leave it as is. If the
letter in the key occurs more than once, the first result is used.

Return the encrypted message.

### Examples

    encrypt("ab c", "abc ab") ➞ "ba cba"
    
    encrypt("otorhinolaryngological", "My name is Paul") ➞ "Mr olme hs Plua"
    
    encrypt("gaderypoluki", "This is an encrypted message") ➞ "Thks ks gn dncyrotde mdssgad"

### Notes

N/A

"""

def encrypt(key, message):
  
  cipher = []
  
  for i in range(0,len(key)-1,2):
    cipher.append(key[i:i+2])
    
  l = list(message)
  
  for i in range(0,len(l)):
    for j in range(0,len(cipher)):
      
      if cipher[j][0]==l[i]:
        l[i]=cipher[j][1]
        break
      elif cipher[j][1]==l[i]:
        l[i]=cipher[j][0]
        break
  return ''.join(l)

