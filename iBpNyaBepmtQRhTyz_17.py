"""


The columnar cipher is a transposition cipher that works like this.

Start with a secret message:

    msg = "Meet me by the lake at midnight. Bring shovel."

Transform uppercase letters into lowercase and remove punctuation and spaces:

    msg = "meetmebythelakeatmidnightbringshovel"

Then, pick a keyword made out of distinct letters:

    keyword = "python"

Break up the message into chunks of the same length as the keyword, and write
them in rows under the keyword. Then, number the columns based on the
alphabetised order of the letters in the keyword:

p| y| t| h| o| n  
---|---|---|---|---|---  
m| e| e| t| m| e  
b| y| t| h| e| l  
a| k| e| a| t| m  
i| d| n| i| g| h  
t| b| r| i| n| g  
s| h| o| v| e| l  
4| 6| 5| 1| 3| 2  
  
Read off the enciphered message (ciphertext) from the columns, in the order
specified by the numbers:

    ciphertext = "thaiivelmhglmetgnembaitsetenroeykdbh"

If the message length is not a multiple of the keyword length, fill in each
blank space with "x". For example:

    msg = "Meet me at midnight."
    
    keyword = "python"

p| y| t| h| o| n  
---|---|---|---|---|---  
m| e| e| t| m| e  
a| t| m| i| d| n  
i| g| h| t| x| x  
  
Create a function that takes a string and a keyword. Return the ciphertext if
the string is in plaintext (i.e. broken up into normal English words and
punctuated), or the deciphered message if the string is in ciphertext. The
resulting deciphered message will not have spaces.

### Examples

    c_cipher("Meet me by the lake at midnight. Bring shovel.", "python")
    ➞ "thaiivelmhglmetgnembaitsetenroeykdbh"
    
    c_cipher("meeanbsleyamgioxebltirhxttkihnvxmhedtgex", "monty")
    ➞ "meetmebythelakeatmidnightbringshovelxxxx"
    
    c_cipher("Mission Delta Kilo Sierra has been compromised. Kill Steve. Evacuate", "cake")
    ➞ "ioliiabcrsiteuxmieksrsnpiksecesdaoraemmdlvatxsntleheooelevax"

### Notes

N/A

"""

def c_cipher(msg, keyword):
  def encode_or_decode(msg):
    uppercase = list('abcdefghijklmnopqrstuvwxyz'.upper())
    
    for l8r in uppercase:
      if l8r in msg:
        return 'E'
    
    if ' ' in msg:
      return 'E'
    
    return 'D'
  class Cipher:
​
    def __init__(self, key):
      self.key = key
    
    def encrypt(self, msg):
​
      msg = msg.lower()
      to_remove = list('.,!?/')
​
      for item in to_remove:
        if item in msg:
          msg = msg.replace(item, '')
      
      msg = ''.join(msg.split())
      print(msg)
      columns = {}
​
      count = 0
​
      for n in range(len(msg)):
        l8r = msg[n]
        if self.key[count] not in columns.keys():
          columns[self.key[count]] = [l8r]
        else:
          columns[self.key[count]].append(l8r)
        count += 1
        if count >= len(self.key):
          count = 0
      
      values = {}
      a = list('abcdefghijklmnopqrstuvwxyz')
​
      for n in range(len(a)):
        l8r = a[n]
        if l8r in self.key:
          values[n] = l8r
      
      goal_length = max([len(l) for l in list(columns.values())])
​
      for column in columns.keys():
        col = columns[column]
        while len(col) < goal_length:
          col.append('x')
        columns[column] = col
      
      new_order = []
​
      for value in sorted(list(values.keys())):
        ident = values[value]
        new_order.append(''.join(columns[ident]))
      
      return ''.join(new_order)
​
    def decrypt(self, msg):
​
      msg = list(msg)
      len_of_columns = int(len(msg) / len(self.key))
​
      columns = []
​
      for n in range(len(self.key)):
        column = []
        for num in range(len_of_columns):
          column.append(msg[0])
          msg.pop(0)
        columns.append(column)
      
      l8r_vals = {}
      a = list('abcdefghijklmnopqrstuvwxyz')
​
      for n in range(26):
        l8r = a[n]
        if l8r in self.key:
          l8r_vals[n] = l8r
      
      column_id = {}
      index = 0
​
      for val in sorted(list(l8r_vals.keys())):
        column_id[l8r_vals[val]] = columns[index]
        index += 1
      
      rows = []
​
      for n in range(len_of_columns):
        row = []
        for val in self.key:
          col = column_id[val]
          row.append(col[n])
        rows.append(''.join(row))
      
      return ''.join(rows)
​
  cipher = Cipher(keyword)
​
  eod = encode_or_decode(msg)
​
  if eod == 'E':
    return cipher.encrypt(msg)
  elif eod == 'D':
    return cipher.decrypt(msg)
  else:
    return 'EOD error! {}'.format(eod)

