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

def get_rectangle(table, digram):
    for row in range(5):
        for col in range(5):
            if table[row][col] == digram[0]:
                coord1 = (row, col)
            elif table[row][col] == digram[1]:
                coord2 = (row, col)
    return coord1, coord2
​
def digram_to_digram_encrypt(table, digram):
    coord1, coord2 = get_rectangle(table, digram)
    if coord1[0] == coord2[0]:
        # letters in same row of table:
        if coord1[1] == 4:
            c1 = table[coord1[0]][0]
        else:
            c1 = table[coord1[0]][coord1[1]+1]
        if coord2[1] == 4:
            c2 = table[coord1[0]][0]
        else:
            c2 = table[coord1[0]][coord2[1]+1]
    elif coord1[1] == coord2[1]:
        # letters in same column of table:
        if coord1[0] == 4:
            c1 = table[0][coord1[1]]
        else:
            c1 = table[coord1[0]+1][coord1[1]]
        if coord2[0] == 4:
            c2 = table[0][coord1[1]]
        else:
            c2 = table[coord2[0]+1][coord2[1]]
    else:
        # letters not in same row or column:
        c1 = table[coord1[0]][coord2[1]]
        c2 = table[coord2[0]][coord1[1]]
    return c1 + c2
​
def generate_table(key):
    chars = [chr(k) for k in range(65, 91)]
    table = [[None for _ in range(5)] for __ in range(5)]
    row, col = 0, 0
    for k in key:
        if not 'A' <= k <= 'Z' or k not in chars:
            continue
        table[row][col] = k
        chars.remove(k)
        col += 1
        if col == 5:
            col = 0
            row += 1
    for c in chars:
        if c == 'J':
            continue
        table[row][col] = c
        col += 1
        if col == 5:
            col = 0
            row += 1
    table1, table2 = {}, {}
    for i in range(65, 91):
        for j in range(65, 91):
            if i != j:
                digram1 = chr(i) + chr(j)
                if 'J' not in digram1:
                    digram2 = digram_to_digram_encrypt(table, digram1)
                    table1[digram1] = digram2
                    table2[digram2] = digram1
    return table1, table2
​
def playfair_encode(message, key):
    table1, table2 = generate_table(key)
    message = [char for char in message if 'A' <= char <= 'Z']
    cipher = ""
    while len(message) > 0:
        char1 = message.pop(0)
        if len(message) > 0 and message[0] != char1:
            char2 = message.pop(0)
        else:
            char2 = 'X'
        digram = char1 + char2
        digram2 = table1[digram]
        cipher += digram2
    return cipher
​
def playfair_decode(cipher, key):
    table1, table2 = generate_table(key)
    cipher = [char for char in cipher if 'A' <= char <= 'Z']
    msg = ""
    while len(cipher) > 0:
        char1 = cipher.pop(0)
        if len(cipher) > 0 and cipher[0] != char1:
            char2 = cipher.pop(0)
        else:
            char2 = 'X'
        digram = char1 + char2
        digram2 = table2[digram]
        msg += digram2
    return msg
​
def playfair(txt, keyword):
    if all(['A' <= c <= 'Z' for c in txt]):
        # cipher given, so decipher:
        txt = txt.replace('J', 'I')
        keyword = keyword.upper()
        msg = playfair_decode(txt, keyword)
        return msg
    else:
        # plaintext given, so encipher:
        txt = ''.join([c for c in txt.upper() if 'A' <= c <= 'Z']).replace('J', 'I')
        keyword = keyword.upper()
        cipher = playfair_encode(txt, keyword)
        return cipher

