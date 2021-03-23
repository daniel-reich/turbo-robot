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

from string import ascii_uppercase
​
def playfair(txt, keyword):
    ## Format strings
    
    decipher = False
    if txt.isalpha() and txt.isupper():
        decipher = True
    else:
        txt = txt.upper()
        aux = []
        for a in txt:
            if a.isalpha():
                aux.append(a)
        txt = "".join(aux)
    
    keyword = keyword.upper()
    keyword = "".join([j for i, j in enumerate(keyword) if j not in keyword[:i]])
    
    ## Create polybius square
    
    n = 5
    char_list = list(keyword) + [c for c in ascii_uppercase if c not in keyword]
    char_list.remove('J')
    
    square = [[""]*n for i in range(n)]
    for i in range(n):
        row = []
        for j in range(n):
            c = char_list[j + n*(i)]
            if c != 'J':
                square[i][j] = c
    
    ## Prepare digraphs
    
    digraphs = []
    i = 0
    while i < len(txt):
        if i == len(txt)-1 or txt[i] == txt[i+1]:
            digraphs.append((txt[i] if txt[i] != "J" else "I", "X"))
            i += 1
        else:
            digraphs.append((txt[i] if txt[i] != "J" else "I", txt[i+1] if txt[i] != "J" else "I"))
            i += 2
    print(digraphs)
    
    ## Cipher
    
    c_digraphs = []
    for d in digraphs:
        first = None
        second = None
        for i, row in enumerate(square):
            if first is None:
                first = (i, row.index(d[0])) if d[0] in row else None
            if second is None:
                second = (i, row.index(d[1])) if d[1] in row else None
            if first and second:
                break
            
        if first[0] == second[0]:
            if decipher:
                c_digraphs.append(((square[first[0]][first[1]-1] if first[1]-1 >= 0 else square[first[0]][-1]),
                    (square[second[0]][second[1]-1] if second[1]-1 >= 0 else square[second[0]][-1])))
            else:
                c_digraphs.append(((square[first[0]][first[1]+1] if first[1]+1 < len(square[0]) else square[first[0]][0]),
                    (square[second[0]][second[1]+1] if second[1]+1 < len(square[0]) else square[second[0]][0])))
        elif first[1] == second[1]:
            if decipher:
                c_digraphs.append(((square[first[0]-1][first[1]] if first[0]-1 >= 0 else square[-1][first[1]]),
                    (square[second[0]-1][second[1]] if second[0]-1 >= 0 else square[-1][second[1]])))
            else:
                c_digraphs.append(((square[first[0]+1][first[1]] if first[0]+1 < len(square) else square[0][first[1]]),
                    (square[second[0]+1][second[1]] if second[0]+1 < len(square) else square[0][second[1]])))
        else:
            c_digraphs.append((square[first[0]][second[1]], square[second[0]][first[1]]))
    return "".join(list(map(lambda x: x[0]+x[1], c_digraphs)))

