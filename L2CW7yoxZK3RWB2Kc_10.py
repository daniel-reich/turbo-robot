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

from math import ceil
​
def ordering(key):
  indices = []
​
  for c in sorted(key):
    i = 0
    while True:
      i = key.index(c, i)
      if i not in indices: break
      i += 1
    indices.append(i)
​
  return indices
​
def nico_cipher(message, key):
  x = [[k, []] for k in key]
​
  n = ceil(len(message) / len(key)) * len(key)
  for i in range(n):
    x[i % len(key)][1].append(message[i] if i < len(message) else " ")
​
  order = ordering(key)
  res = ""
  for i in range(n):
    res += x[order[i % len(key)]][1].pop(0)
​
  return res

