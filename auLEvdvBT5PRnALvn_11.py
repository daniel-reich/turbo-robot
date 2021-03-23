"""


In **Mirror Cipher** , encoding is done by switching message characters with
its mirror opposite character of the key.

Create a function that takes two arguments; a `message` and an optional `key`,
and return the **encoded message**.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    message = "Mubashir Hassan"
    key = "edabitisamazing"
    
    mirror_cipher(message, key) ➞ "tuzishar hissid"

 **Step 1:** Replace all characters of the given message with mirror character
in the key:

    M = t, # 't' is mirror character of 'M'
    u = u, # 'u' is not part of the key
    b = z, # 'z' is mirror character of 'b'
    a = i, and so on ...

 **Step 2:** Return encoded message in lower case:

    "tuzishar hissid"

If optional `key` is not given, consider the whole alphabet as a default (i.e.
`key` = **"abc..z"** ).

### Examples

    mirror_cipher("Mubashir Hassan", "edabitisamazing") ➞ "tuzishar hissid"
    
    mirror_cipher("Matt MacPherson") ➞ "nzgg nzxksvihlm"
    
    mirror_cipher("Airforce is best", "pilot") ➞ "aorfirce os besp"

### Notes

Ignore case of message and key, (e.g. "M" = "m").

"""

from string import ascii_lowercase as al
def mirror_cipher(message, key=al):
  message, key = message.lower(), key.lower()
  result = ""
  for letter in message:
    if not letter in key:
      result += letter
    else:
      index = key.find(letter)
      mirror = key[-index-1]
      result += mirror
  return result

