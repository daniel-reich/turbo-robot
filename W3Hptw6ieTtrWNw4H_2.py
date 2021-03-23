"""


The basic **Polybius Square** is a 5x5 square grid with the letters A-Z
written into the grid. "I" and "J" typically share a slot (as there are 26
letters and only 25 slots).

| 1| 2| 3| 4| 5  
---|---|---|---|---|---  
 **1**|  A| B| C| D| E  
 **2**|  F| G| H| I/J| K  
 **3**|  L| M| N| O| P  
 **4**|  Q| R| S| T| U  
 **5**|  V| W| X| Y| Z  
  
The **Bifid** cipher uses the Polybius square but adds a layer of complexity.

Start with a secret message. Remove spaces and punctuation.

    plaintext = "ikilledmufasa"

Encipher the message using the basic Polybius cipher (see my [previous
challenge](https://edabit.com/challenge/2C3gtb4treAFyWJMg) — right click and
select "open in new tab"), but write the numbers in two rows under the
message, like so:

i| k| i| l| l| e| d| m| u| f| a| s| a  
---|---|---|---|---|---|---|---|---|---|---|---|---  
2| 2| 2| 3| 3| 1| 1| 3| 4| 2| 1| 4| 1  
4| 5| 4| 1| 1| 5| 4| 2| 5| 1| 1| 3| 1  
  
Read off the numbers horizontally, in pairs:

    22 23 31 13 42 14 14 54 11 54 25 11 31

Generate the ciphertext by converting these new pairs of numbers into new
letters using the Polybius square.

    ciphertext = "ghlcrddyaykal"

Create a function that takes a plaintext or ciphertext, and returns the
corresponding ciphertext or plaintext.

### Examples

    bifid("I killed Mufasa!") ➞ "ghlcrddyaykal"
    
    bifid("ghlcrddyaykal") ➞ "ikilledmufasa"
    
    bifid("hi") ➞ "go"

### Notes

N/A

"""

def bifid(text):
  def polybius_square(txt, c):#My code from the first Polybius Square 
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
    
    if c == 'E':
      tr = encrypt(txt.upper(), rows, cols)
    elif c == 'D':
      tr = decrypt(txt, rows, cols)
    else:
      return 'UNKNOWN ERROR!!!'
​
    return tr
  def b_encode(square):
​
​
    row1 = []
    row2 = []
​
    for n in range(0, len(square), 2):
      row1.append(int(square[n]))
      row2.append(int(square[n + 1]))
    
    new_l8rs = []
    rows = row1
​
    for item in row2:
      rows.append(item)
    del row2
    del row1
​
    
    for n in range(0, len(rows), 2):
      
      n1 = rows[n]
      n2 = rows[n + 1]
​
      l8r = '{}{}'.format(n1, n2)
​
      new_l8rs.append(l8r)
    
    return ''.join(new_l8rs)
  def b_decode(square):
​
    rows = square
​
    half = len(square) / 2
​
    row1 = []
    row2 = []
​
    for n in range(0, len(square)):
      item = rows[n]
      if n < half:
        row1.append(item)
      else:
        row2.append(item)
    
    if len(row1) != len(row2):
      return 'ERROR'
    
    decoded = []
    for n in range(0, len(row1)):
​
      r1 = row1[n]
      r2 = row2[n]
​
      d = r1 + r2 
​
      decoded.append(d)
    
    return ''.join(decoded)
  def choose(txt, a):
​
    to_do = 'D'
  
    for item in txt:
      if item not in a:
        to_do = 'E'
        break
​
    return to_do
​
  
  txt = ''
  a = 'a b c d e f g h i k l m n o p q r s t u v w x y z'.split()
  c = choose(text, a)
  
  for item in text:
    if item in a or item.lower() in a:
      txt += item.lower()
    else:
      try:
        test = int(item)
        txt += item
      except ValueError:
        continue
  del text
​
  
  ps = polybius_square(txt, 'E')
  
  if c == 'E':
    be = b_encode(ps)
  elif c == 'D':
    be = b_decode(ps)
  else:
    return 'UNKNOWN ERROR'
    
  ps2 = polybius_square(be, 'D')
​
  return ps2

