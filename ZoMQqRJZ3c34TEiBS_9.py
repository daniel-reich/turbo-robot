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

def playfair(txt, key):
  encoded = False if ' ' in txt else True
  polybius = get_deranged_polybius(key)
  txt = adjust_doubles(txt)
​
  if not encoded:
    return encode_decode(polybius,txt)
  else:
    return encode_decode(polybius,txt,decode=True)
​
def encode_decode(polybius,txt,decode=False):
  adj = -1 if decode else 1
  res = ''
  for a, b in txt:
    a = get_index(polybius,a)
    b = get_index(polybius,b)
​
    if a[0] == b[0]:
      ax,ay = [a[0],(a[1]+adj)%5]
      bx,by = [b[0],(b[1]+adj)%5]
    elif a[1] == b[1]:
      ax,ay = [(a[0]+adj)%5,a[1]]
      bx,by = [(b[0]+adj)%5,b[1]]
    else:
      ax,ay = [a[0],b[1]]
      bx,by = [b[0],a[1]]
​
    res += polybius[ax][ay] + polybius[bx][by]
  return res
​
def get_index(polybius,letter):
  for i, j in enumerate(polybius):
    if letter in j:
      return (i,j.index(letter)) 
​
def adjust_doubles(txt):
  txt = [i for i in txt.upper() if i.isalpha()]
  txt = [''.join(txt[i:i+2]) for i in range(0,len(txt),2)]
​
  while any(len(set(i))==1 and len(i)==2 for i in txt):
    for i in range(len(txt)):
      if len(set(txt[i]))==1:
        txt[i] = txt[i][0] + 'X' + txt[i][1]
        break
    txt = ''.join(i for i in txt)
    txt = [''.join(txt[i:i+2]) for i in range(0,len(txt),2)]
  if len(txt[-1]) != 2:
    txt[-1] += 'X'
  return txt
​
def get_deranged_polybius(key):
  res = []
  for ch in key.upper() + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
    if ch not in res:
      res.append(ch)
  return [res[i:i+5] for i in range(0,25,5)]

