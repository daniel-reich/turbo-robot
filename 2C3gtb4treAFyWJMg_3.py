"""


The **Polybius Square** cipher is a simple substitution cipher that makes use
of a 5x5 square grid. The letters A-Z are written into the grid, with "I" and
"J" typically sharing a slot (as there are 26 letters and only 25 slots).

| 1| 2| 3| 4| 5  
---|---|---|---|---|---  
 **1**|  A| B| C| D| E  
 **2**|  F| G| H| I/J| K  
 **3**|  L| M| N| O| P  
 **4**|  Q| R| S| T| U  
 **5**|  V| W| X| Y| Z  
  
To encipher a message, each letter is merely replaced by its row and column
numbers in the grid.

Create a function that takes a plaintext or ciphertext message, and returns
the corresponding ciphertext or plaintext.

### Examples

    polybius("Hi") ➞ "2324"
    
    polybius("2324  4423154215") ➞ "hi there"
    
    polybius("543445 14343344 522433 21422415331443 52244423 4311311114") ➞ "you dont win friends with salad"

### Notes

  * As "I" and "J" share a slot, both are enciphered into 24, but deciphered only into "I" (see third and fourth test).
  * Any charactor other than letters and spaces should be dropped from the cypher.

"""

def polybius(txt):
  def choose(txt):#This function tests to see if the txt is encoded or decoded. It uses the fact that an encoded message will be made up solely of numbers to it's advantage!
    result = 'D'
    txt = txt.split()
    for n in range(0, len(txt)):
      item = txt[n]
      try:
        i = int(item)
      except ValueError:
        result = 'E'
        break
    
    return result  
  def encrypt(txt, rows, cols):
    
    a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split()
    encrypted = ''
    
    for l8r in txt:
      if l8r in a:
        if l8r == 'J':
          l8r = 'I'
​
        row = None
        col = None
        
        for n in range(1, 6):
          rowtest = rows[n]
          coltest = cols[n]
​
          if l8r in rowtest:
            row = n
          if l8r in coltest:
            col = n
          
          if row != None and col != None:
            break
        
        if row == None:
          return 'error finding row'.upper()
        if col == None:
          return 'error finding col'.upper()
​
        el8r = '{r}{c}'.format(r = row, c = col)
​
        encrypted += el8r
      else:
        if l8r == ' ':
          encrypted += l8r
    
    return encrypted
  def decrypt(cipher, rows, cols):
​
    words = cipher.split()
​
    unencrypted_words = []
​
    for word in words:
​
      w = ''
​
      for n in range(0, len(word), 2):
        
        rowid = int(word[n])
        colid = int(word[n + 1])
​
        row = rows[rowid]
        col = cols[colid]
​
        for letter in row:
          if letter in col:
            l8r = letter
            break
        
        w += l8r
​
      unencrypted_words.append(w)
    
    unencrypted = ' '.join(unencrypted_words)
​
    return unencrypted.lower()
  
  rows = {1: 'A B C D E'.split(), 2: 'F G H I K'.split(), 3: 'L M N O P'.split(), 4: 'Q R S T U'.split(), 5: 'V W X Y Z'.split()}
  cols = {}
​
  for n in range(0, 5):
    col = []
    for num in range(1, 6):
      row = rows[num]
      item = row[n]
      col.append(item)
    cols[n + 1] = col
  
  c = choose(txt)
  
  if c == 'E':
    tr = encrypt(txt.upper(), rows, cols)
  elif c == 'D':
    tr = decrypt(txt, rows, cols)
  else:
    return 'UNKNOWN ERROR!!!'
​
  return tr

