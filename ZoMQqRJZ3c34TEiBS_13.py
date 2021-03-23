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

def createPolybiusSquare(keyword):
  k, keyword_ended,kk,psq,counter=0,False,0,[['' for i in range(5)] for j in range(5)],0
  for i in range (5):
    j=0
    while j<5:
      if k<len(keyword):
        psq[i][j]=keyword[k].upper()
        k+=1
        j+=1
      else:
        if not (chr(65+kk) in keyword.upper() or chr(65+kk)=='J'):
          psq[i][j]=chr(65+kk)
          kk+=1
          j+=1
        else:
          kk+=1
  return psq
  
def bigramsCreation(txt):
  i=extra=0
  bigrams,letters ='',''
  while i< len(txt)-1:
    if txt[i]==txt[i+1]:
      bigrams+=txt[i]+'x'+ ' ' + txt[i+1]
      letters+=txt[i]+txt[i+1]
      extra=1
      i+=2
    else:
      if extra==1:
        bigrams+=txt[i]+ ' '
        letters+=txt[i]
        extra=0
        i+=1
      else:
        bigrams+=txt[i]+txt[i+1]+' '
        letters+=txt[i]+txt[i+1]
        i+=2
        
  if len(letters) < len (txt):
    bigrams+=txt[-1]+'x'
  return bigrams
​
​
def playfair(txt, keyword):
  keyword1=''
  for c in keyword:
    if not c in keyword1:
      keyword1+=c
  psq= createPolybiusSquare(keyword1)
  if (txt.split()[0]==txt):
    cipher=False
  else:
    cipher=True
  txt1,out= ''.join([c[i].lower() for c in txt.split() for i in range (len(c)) if c[i].isalpha()]),''
  bigrams = bigramsCreation(txt1)
  for bi in bigrams.split():
    col_or_row=False
    for i in psq:
      if bi[0].upper() in i and bi[1].upper() in i:
        col_or_row=True
        if (cipher):
          for k in range (2):
            if i.index(bi[k].upper())+1 <=4:
              out+= i[i.index(bi[k].upper())+1]
            else:
              out+= i[(i.index(bi[k].upper())+1)%5]
        else:
          for k in range (2):
            if i.index(bi[k].upper())-1 >=0:
              out+= i[i.index(bi[k].upper())-1]
            else:
              out+= i[4]
​
    for j in range(5):
      if (col_or_row):
        break
      col=[]
      for i in psq:
        col.append(i[j])
      if bi[0].upper() in col and bi[1].upper() in col:
        col_or_row=True
        for k in range (2):
          if cipher:
            if col.index(bi[k].upper())+1 <=4:
              out+= col[col.index(bi[k].upper())+1]
            else:
              out+= col[(col.index(bi[k].upper())+1)%5]
          else:
            if col.index(bi[k].upper())-1 >=0:
              out+= col[col.index(bi[k].upper())-1]
            else:
              out+= col[4]
​
    if not (col_or_row):
      for i in range (5):
        for j in range (5):
          if bi[0].upper() == psq[i][j]:
            one=(i,j)
          if bi[1].upper() == psq[i][j]:
            two=(i,j)
      out+=psq[one[0]][two[1]]
      out+=psq[two[0]][one[1]]
  
  return out

