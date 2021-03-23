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
  a = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
  temp = ''
  for i in keyword:
    if i not in temp:
      temp += i
  keyword = temp
  txt,keyword = txt.upper(), keyword.upper()
  txt = ''.join([i for i in txt if i in a or i == ' '])
  for i in a:
    if i not in keyword:
      keyword += i
  it = 0  
  lst = [''] * 5
  for i in range(len(lst)):
    lst[i] = [''] * 5
  for i in range(len(lst)):
    for x in range(5):
      lst[i][x] = keyword[it]
      it += 1
  columns = []
  for i in range(len(lst[0])):
    columns.append(''.join([a[i] for a in lst]))
  rows = [''.join(i) for i in lst]
  if ' ' in txt:
    txt = txt.replace(' ','')
    pairs = [txt[i:i+2] for i in range(0,len(txt),2)]
    while not all([len(set(i)) != 1 for i in pairs]):
      pairs = ''.join(pairs)
      indexes = []
      check = False
      for i in range(1,len(pairs)):
        if pairs[i] == pairs[i-1] and i%2 == 1:
          indexes.append(i)
          check = True
      if check:
        pairs = pairs[:indexes[0]]+'X'+pairs[indexes[0]:]
      else:
        pairs += 'X'
      pairs = [pairs[i:i+2] for i in range(0,len(pairs),2)]
    for i in range(len(pairs)):
      a,b = pairs[i][0],pairs[i][1]
      check = False
      for x in range(5):
        if a in rows[x] and b in rows[x]:
          pairs[i] = rowfix(a,b,rows[x],'encode')
          check = True
        elif a in columns[x] and b in columns[x]:
          pairs[i] = colfix(a,b,columns[x],'encode')
          check = True
        if not check:
          pairs[i] = squarefix(a,b,lst)
  else:
    pairs = [txt[i:i+2] for i in range(0,len(txt),2)]
    for i in range(len(pairs)):
      a,b = pairs[i][0],pairs[i][1]
      check = False
      for x in range(5):
        if a in rows[x] and b in rows[x]:
          pairs[i] = rowfix(a,b,rows[x],'decode')
          check = True
        elif a in columns[x] and b in columns[x]:
          pairs[i] = colfix(a,b,columns[x],'decode')
          check = True
        if not check:
          pairs[i] = squarefix(a,b,lst)
  return ''.join(pairs)
  
def rowfix(a,b,row,instruction):
  if instruction == 'encode':
    if row.index(a) == 4:
      a = row[0]
    else:
      a = row[row.index(a)+1]
    if row.index(b) == 4:
      b = row[0]
    else:
      b = row[row.index(b)+1]
  elif instruction == 'decode':
    if row.index(a) == 0:
      a = row[4]
    else:
      a = row[row.index(a)-1]
    if row.index(b) == 0:
      b = row[4]
    else:
      b = row[row.index(b)-1]
  return a+b
      
def colfix(a,b,col,instruction):
  if instruction == 'encode':
    if col.index(a) == 4:
      a = col[0]
    else:
      a = col[col.index(a)+1]
    if col.index(b) == 4:
      b = col[0]
    else:
      b = col[col.index(b)+1]
  elif instruction == 'decode':
    if col.index(a) == 0:
      a = col[4]
    else:
      a = col[col.index(a)-1]
    if col.index(b) == 0:
      b = col[4]
    else:
      b = col[col.index(b)-1]
  return a+b
      
def squarefix(a,b,lst):
  for i in range(len(lst)):
    for x in range(len(lst[i])):
      if lst[i][x] == a:
        aind = [i,x]
      if lst[i][x] == b:
        bind = [i,x]
  a = lst[aind[0]][bind[1]]
  b = lst[bind[0]][aind[1]]
  return a+b

