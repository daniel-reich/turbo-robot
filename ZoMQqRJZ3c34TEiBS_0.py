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

import numpy as np
​
def playfair(txt, keyword):
    val = 1 if txt[-1] == '.' else -1 # cypher or decypher mode set
    
    board = {chr(val) for val in range(65,91)} # A to Z
    txt = [char for char in txt.upper() if char in board] # Remove space and punctuation
    keyword_f = set(keyword.upper())
    board = np.array(sorted(board - keyword_f)) # (A to Z) - (chars in keyword_f)
    keyword_f = sorted(keyword_f, key = lambda elm: keyword.upper().index(elm)) # sort chars in txt_f in order of their apparition in txt
    board = np.reshape(np.concatenate((keyword_f, np.delete(board, np.where(board == 'J')))), (5,5)) # concatenate txt to board and reshape to a (5*5) array
    
    # insert x between every double letter
    for idx in range(0,len(txt),2):
        try:
            if txt[idx] == txt[idx+1]: txt.insert(idx+1, 'X')
        except: pass
    
    if len(txt)%2 != 0: txt.append('X') # insert x at the end of the message if it the number of chars is odd
    message = np.reshape(txt, (len(txt)//2, 2)) # reshape the message into arrays of 2 chars each
    
    # encrypting the message
    encrypted = ""
    for row in message:
        # get the row and cold of each char in the message
        letter_pos = np.array(list(map(np.concatenate, [np.where(board == row[val]) for val in range(2)])))
        
        # playfair encryption rules
        if letter_pos[0,0] - letter_pos[1,0] == 0: 
            letter_row = letter_pos[0,0]
            encrypted += board[letter_row, (letter_pos[0, 1] + val) % 5] + board[letter_row, (letter_pos[1, 1] + val) % 5]
        elif letter_pos[0,1] - letter_pos[1,1] == 0:
            letter_col = letter_pos[0,1]
            encrypted += board[(letter_pos[0, 0] + val) % 5, letter_col] + board[(letter_pos[1, 0] + val) % 5, letter_col]
        else:
            encrypted += board[letter_pos[0, 0], letter_pos[1,1]] + board[letter_pos[1,0], letter_pos[0,1]]
    
    return encrypted

