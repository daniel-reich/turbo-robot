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

from string import ascii_lowercase as ascl, ascii_uppercase as ascu
​
def caesar_cipher(word, num):
    letter_list = []
    for i in word:
        if i in ascu:
            index = ascu.index(i)
            shifted = index+num-max([i for i in range(0, index+num, len(ascu))])
            letter = ascu[shifted] 
            letter_list.append(letter)          
        elif i in ascl:
            index = ascl.index(i)
            shifted = index+num-max([i for i in range(0, index+num+1, len(ascl))])
            letter = ascl[shifted] 
            letter_list.append(letter)
        else:
            letter_list.append(i)
​
    return "".join(letter_list)

