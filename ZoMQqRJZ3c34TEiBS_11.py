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
  keyword, key = [], keyword
  for i in key: 
    if not i in keyword:
      keyword.append(i)
  keyword = "".join(keyword)
  cipher = [x.upper() for x in keyword] + [chr(x) for x in range(65,91) if chr(x) not in (keyword.upper())+"J" ]
  cipher = [cipher[x:x+5] for x in range(0,25,5)]
  if " " in txt: 
    txt = "".join([x.upper() for x in txt if x.isalnum()])
    while True:
      start = len(txt)
      txt = [txt[x:x+2] for x in range(0, len(txt), 2)]
      for i in range(len(txt)):
        if len(txt[i]) == 1: break
        if txt[i][0] == txt[i][1]:
          txt[i] = txt[i][0]+"X"+txt[i][1]
          break
      txt = "".join(txt)
      if len(txt) == start: break
    if len(txt) % 2 == 1: txt += "X"
    result = ""
    for i in [txt[x:x+2] for x in range(0, len(txt), 2)]:
      for j in range(len(cipher)):
        if i[0] in cipher[j]: left = [cipher[j].index(i[0]), j]
        if i[1] in cipher[j]: right = [cipher[j].index(i[1]), j]
      if left[1] == right[1]: result += cipher[left[1]][(left[0]+1)%5] + cipher[right[1]][(right[0]+1)%5]
      elif left[0] == right[0]: result += cipher[(left[1]+1)%5][(left[0])] + cipher[(right[1]+1)%5][right[0]]
      else: result += cipher[(left[1])][right[0]] + cipher[(right[1])][(left[0])]
  else: 
    result = ""
    for i in [txt[x:x+2] for x in range(0, len(txt), 2)]:
      for j in range(len(cipher)):
        if i[0] in cipher[j]: left = [cipher[j].index(i[0]), j]
        if i[1] in cipher[j]: right = [cipher[j].index(i[1]), j]
      if left[1] == right[1]: result += cipher[left[1]][(left[0]-1)] + cipher[right[1]][(right[0]-1)]
      elif left[0] == right[0]: result += cipher[(left[1]-1)][(left[0])] + cipher[(right[1]-1)][right[0]]
      else: result += cipher[(left[1])][right[0]] + cipher[(right[1])][(left[0])]
  return result

