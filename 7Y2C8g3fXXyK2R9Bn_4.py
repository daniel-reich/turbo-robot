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

import string
def build_alphabet(key):
  alphabet = list(string.ascii_lowercase)
  if not key:
    return alphabet
  prefix = list()
  for k in key:
      if k not in set(prefix):
          prefix.append(k)
  
  return list(prefix) + [x for x in alphabet if x not in set(prefix)]
​
def keyword_cipher(key, message):
    alphabet = build_alphabet(key)
    alphabet_real = set(string.ascii_lowercase)
    return "".join([alphabet[(ord(c)%32)-1] if c in alphabet_real else c for c in message])

