"""


In **Nico Cipher** , encoding is done by creating a numeric key and assigning
each letter position of the message with the provided key.

Create a function that takes two arguments, `key` and `message`, and returns
the **encoded message**.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    message = "mubashirhassan"
    key = "crazy"
    
    nico_cipher(message, key) ➞ "bmusarhiahass n"

 **Step 1:** Assign numbers to sorted letters from the key:

    "crazy" = 23154

 **Step 2:** Assign numbers to the letters of the given message:

    2 3 1 5 4
    ---------
    m u b a s
    h i r h a
    s s a n

 **Step 3:** Sort columns as per assigned numbers:

    1 2 3 4 5
    ---------
    b m u s a
    r h i a h
    a s s   n

 **Step 4:** Return encoded message **Rows-wise** :

    eMessage = "bmusarhiahass n"

### Examples

    nico_cipher("mubashirhassan", "crazy") ➞ "bmusarhiahass n"
    
    nico_cipher("edabitisamazing", "matt") ➞ "deabtiismaaznig "
    
    nico_cipher("iloveher", "612345") ➞ "lovehir    e"

### Notes

Keys will have alphabets or numbers only.

"""

def nico_cipher(message, key):
  index = [i[0] for i in sorted(enumerate(key), key=lambda x:x[1])]
  lk, lm = len(key), len(message)
  n = int(lm / lk)
  r = lk - lm % lk
  msgs = [list(message[i * lk : i * lk +lk]) for i in range(n)]
  msgs += [list(message[n * lk:]) + [' ']*r]
  return ''.join([msg[i] for msg in msgs for i in index])

