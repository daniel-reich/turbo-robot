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

class Nico_Cypher:
​
  def __init__(self, key):
    self.k = key
    self.k_dic = {}
​
    s = sorted(key)
​
    for n in range(len(s)):
      if s[n] not in self.k_dic.keys():
        self.k_dic[s[n]] = [n+1]
      else:
        self.k_dic[s[n]].append(n+1)
    
    
​
  def encrypt(self, msg):
​
    lsts = []
    c = 0
​
    for l8r in msg:
      if len(lsts) < len(self.k):
        lsts.append([l8r])
      else:
        lsts[c%len(self.k)].append(l8r)
      c += 1
    
    goal = max([len(lst) for lst in lsts])
​
    for n in range(len(lsts)):
      lst = lsts[n]
      while len(lst) < goal:
        lst.append(' ')
      lsts[n] = lst
    
    l8r_indexes = {l8r:0 for l8r in set(self.k)}
    lst_indexes = {}
    lst_ind = 0
​
    for l8r in self.k:
      
      lst_indexes[self.k_dic[l8r][l8r_indexes[l8r]]] = lsts[lst_ind]
      l8r_indexes[l8r] += 1
      lst_ind += 1
    
    tr = ''
​
    for n in range(goal):
      for k in sorted(lst_indexes.keys()):
        tr += lst_indexes[k][n]
    
    return tr
def nico_cipher(msg, key):
  
  cypher = Nico_Cypher(key)
  return cypher.encrypt(msg)

