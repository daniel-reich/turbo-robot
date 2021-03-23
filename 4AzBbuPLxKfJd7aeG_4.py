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
    original_letter = []
    encrypted_letter = []
    for i in range(len(key)):
        if key[i].lower() not in original_letter:
            original_letter.append(key[i].lower())
            if i%2 == 0:
                encrypted_letter.append(key[i+1].lower())
            else:
                encrypted_letter.append(key[i-1].lower())
​
    encrypted_message = ""
    for i in range(len(message)):
        capital = message[i].isupper()
        if message[i].lower() in original_letter:
            for index, letter in enumerate(original_letter):
                if letter == message[i].lower():
                    if capital:
                        encrypted_message += encrypted_letter[index].upper()
                    else:
                        encrypted_message += encrypted_letter[index]
                    break
        else:
            encrypted_message += message[i]
            
    return(encrypted_message)

