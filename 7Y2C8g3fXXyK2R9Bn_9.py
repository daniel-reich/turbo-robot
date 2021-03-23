"""


A **Keyword Cipher** is a monoalphabetic cipher which uses a keyword to
provide encryption on given string of message.

Create a function that takes two arguments; a string of `message` and a string
of `key` and returns an **encoded message**.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    message = "ABCHIJ"
    key = "KEYWORD"
    
    keyword_cipher(key, message) ➞ "KEYABC"

Write all alphabets from A to Z:

| | | | | | | | | | | | | | | | | | | | | | |  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
A| B| C| D| E| F| G| H| I| J| K| L| M| N| O| P| Q| R| S| T| U| V| W| X| Y| Z  
  
All alphabets which are part of keyword are removed and the alphabets are re-
arranged such that keyword appears first, followed by the rest of the
alphabets in usual order.

| | | | | | | | | | | | | | | | | | | | | | |  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
K| E| Y| W| O| R| D| A| B| C| F| G| H| I| J| L| M| N| P| Q| S| T| U| V| X| Z  
  
Return all alphabets of key against given message:

    eMessage = "KEYABC"
    // A = K, B = E, C = Y, H = A, I = B, J = C

### Examples

    keyword_cipher("keyword", "abchij") ➞ "keyabc"
    
    keyword_cipher("purplepineapple", "abc") ➞ "pur"
    
    keyword_cipher("mubashir", "edabit") ➞ "samucq"

### Notes

  * Don't forget to remove duplicates after concatenating string with keyword.
  * Take care of characters other than alphabets.

"""

class Cipher:
​
  l8rs = 'abcdefghijklmnopqrstuvwxyz'
​
  def __init__(self, keyword):
    self.k = []
​
    for l8r in keyword:
      if l8r not in self.k:
        self.k.append(l8r)
​
    self.new_alph = ''.join(self.k + [l8r for l8r in Cipher.l8rs if l8r not in keyword])
​
    self.encrypt_dic = {Cipher.l8rs[n]: self.new_alph[n] for n in range(26)}
    self.decrypt_dic = {self.new_alph[n]: Cipher.l8rs[n] for n in range(26)}
​
  def encrypt(self, msg):
    try:
      return ''.join([self.encrypt_dic[l8r] for l8r in msg])
    except KeyError:
      tr = []
​
      for l8r in msg:
        try:
          tr.append(self.encrypt_dic[l8r])
        except KeyError:
          tr.append(l8r)
      
      return ''.join(tr)
  
  def decrypt(self, msg):
    try:
      return ''.join([self.decrypt_dic[l8r] for l8r in msg])
    except KeyError:
      tr = []
​
      for l8r in msg:
        try:
          tr.append(self.decrypt_dic[l8r])
        except KeyError:
          tr.append(l8r)
        
      return ''.join(tr)
​
​
​
def keyword_cipher(key, msg):
​
  cipher = Cipher(key)
​
  return cipher.encrypt(msg)

