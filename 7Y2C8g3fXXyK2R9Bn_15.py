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

def keyword_cipher(key, message):
  k = ''
  for i in key:
    if i not in k:
      k+=i
  abc = 'abcdefghijklmnopqrstuvwxyz'
  for i in k:
    abc = abc.replace(i,'',1)
  new_abc = (k+abc)[:26]
  return ''.join(new_abc[ord(i)-97] if 0<=ord(i)-97<=26 else i for i in message)

