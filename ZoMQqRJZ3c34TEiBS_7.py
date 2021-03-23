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
    key_upper = keyword.upper().replace('J', 'I')
    lst_key = sorted([c for c in set(key_upper)], key=key_upper.index)
    alphabet = list(chr(65 + i) for i in range(26) if chr(65 + i) != 'J')
    alphabet_no_key = sorted(list(set(alphabet) - set(lst_key)),
                             key=alphabet.index)
    polybius = lst_key + alphabet_no_key
​
    def coordinates(letter):
        idx = polybius.index(letter)
        return idx // 5, idx % 5
​
    def letter_by_row_col(r, c):
        return polybius[r * 5 + c]
​
    def digraphs(s):
        s = s.upper().replace('J', 'I')
        lst = [c for c in s if c.isalpha()]
        change = True
        while change:
            change = False
            for i in range(0, len(lst) - 1, 2):
                if lst[i] == lst[i + 1]:
                    lst = lst[: i + 1] + ['X'] + lst[i + 1:]
                    change = True
                    break
        if len(lst) % 2:
            lst.append('X')
        return lst
​
    res, shift = '', 1
    if ' ' in txt:
        lst_digraphs = digraphs(txt)
    else:
        lst_digraphs = [c for c in txt]
        shift = -1
    for i in range(0, len(lst_digraphs) - 1, 2):
        a_row, a_col = coordinates(lst_digraphs[i])
        b_row, b_col = coordinates(lst_digraphs[i + 1])
        if a_row == b_row:
            res += letter_by_row_col(a_row, (a_col + shift) % 5)
            res += letter_by_row_col(b_row, (b_col + shift) % 5)
        elif a_col == b_col:
            res += letter_by_row_col((a_row + shift) % 5, a_col)
            res += letter_by_row_col((b_row + shift) % 5, b_col)
        else:
            res += letter_by_row_col(a_row, b_col)
            res += letter_by_row_col(b_row, a_col)
    return res

