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
    keys = [key[i:i + 2] for i in range(0, len(key), 2)]
    output = ''
    for i in message:
        found = 0
        for j in keys:
            if i in j:
                output += j.replace(i, '')
                found = 1
                break
        if not found:
            output += i
    return output

