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

import re
​
def playfair(txt, keyword):
  grid = []
  temp = []
  letters = list("abcdefghijklmnopqrstuvwxyz")
  for i in keyword:
    if i in letters:
      if i == "i" or i == "j":
        letters.remove("i")
        letters.remove("j")
        temp.append("ij")
      else:
        letters.remove(i)
        temp.append(i)
      if len(temp) == 5:
        grid.append(temp)
        temp = []
  for i in letters:
    if i == "j":
      temp.append("ij")
    elif i != "i":
      temp.append(i)
    if len(temp) == 5:
      grid.append(temp)
      temp = []
  decrypt = not re.search("\W",txt) and txt == txt.upper()
  txt = re.sub("\W","",txt).lower()
  i = 0
  while i <= len(txt)-2:
    if txt[i] == txt[i+1] or ((txt[i] == "i" or txt[i] == "j") and (txt[i+1] == "i" or txt[i+1] == "j")):
      txt = txt[:i+1]+"x"+txt[i+1:]
    i += 2
  if len(txt)%2 == 1:
    txt += "x"
  txt = [txt[i:i+2] for i in range(0,len(txt),2)]
  ctxt = ""
  for pair in txt:
    l1, l2 = pair[0], pair[1]
    if l1 == "i" or l1 == "j":
      l1 = "ij"
    if l2 == "i" or l2 == "j":
      l2 = "ij"
    for row in range(len(grid)):
      if l1 in grid[row]:
        row1 = row
        col1 = grid[row].index(l1)
      if l2 in grid[row]:
        row2 = row
        col2 = grid[row].index(l2)
    if row1 == row2:
      if decrypt:
        col1 = (col1-1)%5
        col2 = (col2-1)%5
      else:
        col1 = (col1+1)%5
        col2 = (col2+1)%5
    elif col1 == col2:
      if decrypt:
        row1 = (row1-1)%5
        row2 = (row2-1)%5
      else:
        row1 = (row1+1)%5
        row2 = (row2+1)%5
    else:
      col1, col2 = col2, col1
    l1, l2 = grid[row1][col1], grid[row2][col2]
    if l1 == "ij":
      l1 = "i"
    if l2 == "ij":
      l2 = "i"
    ctxt += l1+l2
  return ctxt.upper()

