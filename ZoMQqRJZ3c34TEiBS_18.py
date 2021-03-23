"""


The **Playfair cipher** is a substitution cipher that uses digraphs (pairs of
letters) instead of single letters, and makes use of symmetrical encryption.

There are some variations on the rules of encipherment. One version of the
cipher rules is outlined below:

  1. A 5x5 _Polybius square_ is constructed, _deranged_ with a keyword.

    keyword = python

  * First, fill in the keyword at the top of the grid, omitting any duplicates (3rd example's keyword has two occurrences of "h". The second one should be omitted).

| | | |  
---|---|---|---|---  
P| Y| T| H| O  
N| | | |  
| | | |  
| | | |  
| | | |  
  * Next, fill in the rest of the slots with the leftover letters of the alphabet that are not in the keyword. Classically, "I" and "J" share a slot (some people elect to omit "Q", "V", or "Z" instead).

| | | |  
---|---|---|---|---  
P| Y| T| H| O  
N| A| B| C| D  
E| F| G| I/J| K  
L| M| Q| R| S  
U| V| W| X| Z  

  2. Remove spaces and punctuation from the message to be enciphered. Then break it up into two-letter chunks (digraphs):

    message = "Tomorrow we attack."
    
    message = "tomorrowweattack"
    
    message = "to mo rr ow we at ta ck"

  3. Digraphs must have two _distinct_ letters. If any digraph consists of the same letter, insert an "x" between them and shift the pairings to the right. Repeat as necessary until all double letters are eliminated. If the resulting message has an odd number of letters, add an "x" to the end.

    message = "to mo rx ro ww ea tt ac k"

Note how shifting the pairings rightward after inserting an 'x' after the
first 'r' has created two more double letter digraphs. Correct them
sequentially.

    message = "to mo rx ro wx we at ta ck"

This insertion corrected both double letter digraphs, and evened out the
message length. No more changes are necessary.

  4. Encipher each digraph into a different digraph by following these 3 rules of encipherment:

  * If the two letters are on the same row, as is the case for the first digraph "to", replace each letter with the letter to its right, wrapping around to the beginning of the row if necessary.

    to -> hp

  * If the two letters are on the same column, as in the third digraph "rx", replace each letter with the letter beneath it, wrapping around to the top if necessary

    rx -> xh

  * If the two letters have dissimilar rows and columns, as in the second digraph "mo", visualise a rectangle with these letters at _opposite_ vertices, then find the other two vertices. Replace each letter with the vertex sharing its row. The original letters are rendered in bold below. The cipher letters are italicised and bolded.

| | | |  
---|---|---|---|---  
P|  ** _Y_**|  T| H|  **O**  
N| A| B| C| D  
E| F| G| I/J| K  
L|  **M**|  Q| R|  ** _S_**  
U| V| W| X| Z  

    mo -> sy
    
    "to mo rx ro wx we at ta ck" -> "hp sy xh sh xz ug by yb di"

Create a function that takes two strings — a plaintext message or ciphertext
`txt`, and a `keyword` — and returns the corresponding ciphertext or
deciphered plaintext (without spaces and with "x" in odd places as
appropriate).

### Examples

    playfair("Tomorrow we attack.", "python") ➞ "HPSYXHSHXZUGBYYBDI"
    
    playfair("HPSYXHSHXZUGBYYBDI", "python") ➞ "TOMORXROWXWEATTACK"
    
    playfair("MYDZABIFBMENFEQAAE", "rhythm") ➞ "THEXEAGLEHASLANDED"

### Notes

Check the **Resources** tab if the explanations here are unclear.

"""

def playfair(txt, keyword):
  def keyword_formatter(keyword):
    
    nk = ''
    for item in keyword:
      if item not in nk:
        nk += item
    return nk
  def square_creator(keyword):
    
    a = 'a b c d e f g h i k l m n o p q r s t u v w x y z'.upper().split()
    keyword = keyword.upper()
    if 'J' in keyword:
      keyword = keyword.replace('J', 'I')
​
    ps = []
​
    n = 0
​
    row = []
​
    for l8r in keyword:
      if n < 4:
        row.append(l8r)
        n += 1
      elif n == 4:
        row.append(l8r)
        ps.append(row)
        row = []
        n = 0
      else:
        return 'UNKNOWN ERROR'
    
    for l8r in a:
      
      if len(row) == 5:
        if row not in ps:
          ps.append(row)
        if l8r not in keyword:
          row = [l8r]
        continue
      
      if len(row) < 5:
        if l8r not in keyword:
          row.append(l8r)
​
    if len(row) != 0:
      if len(row) != 5:
        return 'ERROR L217 {r}{ps}'.format(r = row, ps = ps)
      else:
        ps.append(row)
        del row
    
    return ps
  def choose(txt):
​
    tr = 'D'
​
    for item in txt:
      if item.islower() == True:
        tr = 'E'
        break
​
    return tr
  def format_message(txt):
​
    txt = txt.upper()
    a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split()
​
    f1_txt = []
​
    for item in txt:
      if item == 'J':
        f1_txt.append('I')
      elif item in a:
        f1_txt.append(item)
      else:
        continue
    
    f2_txt = []
​
    while len(f1_txt) != 0:
​
      item1 = f1_txt[0]
      try:
        item2 = f1_txt[1]
      except IndexError:
        item2 = 'X'
​
      if item2 == item1:
        item2 = 'X'
        f1_txt.pop(0)
      else:
        f1_txt.pop(0)
        try:
          f1_txt.pop(0)
        except IndexError:
          pass
      
      pair = item1 + item2
​
      f2_txt.append(pair)
    
    return f2_txt
  def digraph_encryptions(digraph, square):
    
    l8r1 = digraph[0]
    l8r2 = digraph[1]
​
    l8r1row = None
    l8r2row = None
    l8r1col = None
    l8r2col = None
    
    for n in range(0, len(square)):
      
      row = square[n]
      if l8r1 in row:
        
        l8r1row = n
        for num in range(0, len(row)):
          item = row[num]
          if item == l8r1:
            l8r1col = num
      if l8r2 in row:
        l8r2row = n 
        for num in range(0, len(row)):
          item = row[num]
          if item == l8r2:
            l8r2col = num
      
      if l8r1row != None and l8r2row != None and l8r2col != None and l8r1col != None:
        break
    
    if l8r1row == l8r2row:
      try:
        row = square[l8r1row]
      except TypeError:
        return l8r1row
      
      if l8r1col + 1 >= 5:
        el8r1 = row[0]
      else:
        el8r1 = row[l8r1col + 1]
      
      if l8r2col + 1 >= 5:
        el8r2 = row[0]
      else:
        el8r2 = row[l8r2col + 1]
      
      tr = el8r1 + el8r2
​
      return tr
    elif l8r1col == l8r2col:
      
      col = []
      colnum = l8r1col
      
      for row in square:
        col.append(row[colnum])
      
      if l8r1row + 1 >= 5:
        el8r1 = col[0]
      else:
        el8r1 = col[l8r1row + 1]
      
      if l8r2row + 1 >= 5:
        el8r2 = col[0]
      else:
        el8r2 = col[l8r2row + 1]
    
      tr = ''.join([el8r1, el8r2])
​
      return tr
    else:
​
      dl8r1 = square[l8r1row][l8r2col]
      dl8r2 = square[l8r2row][l8r1col]
​
      tr = ''.join([dl8r1, dl8r2])
​
      return tr
  def digraph_decryptions(digraph, square):
​
    l8r1 = digraph[0]
    l8r2 = digraph[1]
​
    l8r1row = None
    l8r1col = None
    l8r2row = None
    l8r2col = None
​
    for n in range(0, len(square)):
      row = square[n]
​
      if l8r1 in row:
        l8r1row = n
        for num in range(0, len(row)):
          titem = row[num]
          if titem == l8r1:
            l8r1col = num
            break
      
      if l8r2 in row:
        l8r2row = n
        for num in range(0, len(row)):
          titem = row[num]
          if titem == l8r2:
            l8r2col = num
            break
​
      if l8r1row != None and l8r2row != None and l8r1col != None and l8r2col != None:
        break
    
    
    if l8r1row == l8r2row:
      row = square[l8r1row]
​
      if l8r1col == 0:
        dl8r1 = row[4]
      else:
        dl8r1 = row[l8r1col - 1]
      
      if l8r2col == 0:
        dl8r2 = row[4]
      else:
        dl8r2 = row[l8r2col - 1]
      
      tr = ''.join([dl8r1, dl8r2])
​
      return tr
    elif l8r1col == l8r2col:
​
      col = []
      for row in square:
        col.append(row[l8r1col])
      
      if l8r1row == 0:
        dl8r1 = col[4]
      else:
        dl8r1 = col[l8r1row - 1]
      
      if l8r2row == 0:
        dl8r2 = col[4]
      else:
        dl8r2 = col[l8r2row - 1]
      
      tr = ''.join([dl8r1, dl8r2])
​
      return tr
    else:
      dl8r1 = square[l8r1row][l8r2col]
      dl8r2 = square[l8r2row][l8r1col]
​
      tr = ''.join([dl8r1, dl8r2])
​
      return tr
​
  c = choose(txt)
  kf = keyword_formatter(keyword)
  sc = square_creator(kf)
  
  if c == 'E':
    fm = format_message(txt)
    
    encrypted = []
​
    for digraph in fm:
      de = digraph_encryptions(digraph, sc)
      encrypted.append(de)
    
    return ''.join(encrypted)
  elif c == 'D':
    fm = format_message(txt)
​
    decrypted = ''
​
    for digraph in fm:
      dd = digraph_decryptions(digraph, sc)
      decrypted += dd
    return decrypted
  else:
    return 'UNKNOWN FINAL ERROR!!!'

