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

def playfair(text, keyword):
    length = len(keyword)
    map_table = []
    for i in range(length):
        if (keyword[i] >='a' and keyword <='z') or (keyword[i] >='A' and keyword <='Z'):
            upper = keyword[i].upper()
            if upper == 'J':
                upper == 'I'
            if upper not in map_table:
                map_table.append(upper)
    for i in range(ord('A'), ord('Z')+1):
        upper = chr(i)
        if upper == 'J':
            upper = 'I'
        if upper not in map_table:
            map_table.append(upper)
    
    plain = []
    length = len(text)
    plain_flag = 1
    count = 0
    for i in range(length):
        if (text[i] >='a' and text[i] <='z') or (text[i] >='A' and text[i] <='Z'):
            plain.append(text[i].lower())
        else:
            plain_flag = 1
        if text[i] >='A' and text[i] <='Z':
            count = count + 1
    
    if count == length:
        plain_flag = 0
        
    
    #split to 2 character block
​
    i = 0
    while(i<len(plain)):
        if (i+1) < len(plain):
            if plain[i] == plain[i+1]:
                 plain.insert(i+1, 'x')
        i = i + 2
    if len(plain)%2 == 1:
        plain.append('x')
                
                
    #encode
    result = []
    length = len(plain)
    for i in range(0, length, 2):
        upper = plain[i].upper()
        if upper == 'J':
            upper = 'I'
        first_index = map_table.index(upper)
        upper = plain[i+1].upper()
        if upper == 'J':
            upper = 'I'
        second_index = map_table.index(upper)
        
        first_row = int(first_index/5)
        first_col = first_index%5
        
        second_row = int(second_index/5)
        second_col = second_index%5
        
        if first_row == second_row:
            if plain_flag == 1:
                first_index_new = first_row*5 + (first_col+1)%5
                second_index_new = second_row*5 + (second_col+1)%5
            else:
                first_index_new = first_row*5 + (first_col+4)%5
                second_index_new = second_row*5 + (second_col+4)%5
            result.append(map_table[first_index_new])
            result.append(map_table[second_index_new])
        elif first_col == second_col:
            if plain_flag == 1:
                first_index_new = ((first_row+1)%5)*5 + first_col
                second_index_new = ((second_row+1)%5)*5 + second_col
            else:
                first_index_new = ((first_row+4)%5)*5 + first_col
                second_index_new = ((second_row+4)%5)*5 + second_col
            result.append(map_table[first_index_new])
            result.append(map_table[second_index_new])
        else:
            first_index_new = first_row*5 + second_col
            second_index_new = second_row*5 + first_col
            result.append(map_table[first_index_new])
            result.append(map_table[second_index_new])
            
    result_str = ""
    for item in result:
        result_str = result_str + item
    return result_str

