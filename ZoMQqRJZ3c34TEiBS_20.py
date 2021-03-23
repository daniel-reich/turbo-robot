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

import string
​
​
def playfair(txt, keyword):
  letters = ''.join(keyword.split()) + string.ascii_lowercase
  square_map = {}
  square = [['' for _ in range(5)] for _ in range(5)]
  row = column = 0
  for letter in letters:
    if letter in square_map:
      continue
    if letter == 'j':
      square_map[letter] = square_map['i']
      continue
    square_map[letter] = (row, column)
    square[row][column] = letter
    if column == 4:
      row += 1
    column = (column + 1) % 5
  text = [letter for word in txt.lower().split() for letter in word if letter.isalpha()]
  pairs = []
  cur_pair = []
  for letter in text:
    if not cur_pair or cur_pair[-1] != letter:
      cur_pair.append(letter)
    else:
      cur_pair.append('x')
      pairs.append(''.join(cur_pair))
      cur_pair = []
      cur_pair.append(letter)
    if len(cur_pair) == 2:
      pairs.append(''.join(cur_pair))
      cur_pair = []
  if cur_pair:
    pairs.append(cur_pair[0] + 'x')
  ciphered = []
  for pair in pairs:
    direction = -1 if txt.isupper() else 1
    letter1, letter2 = [square_map[letter] for letter in pair]
    if letter1[0] == letter2[0]:
      row = letter1[0]
      new_coords = [(coord + direction) % 5 for coord in (letter1[1], letter2[1])]
      new_pair = ''.join([
        square[row][column] for column in new_coords
      ])
    elif letter1[1] == letter2[1]:
      column = letter1[1]
      new_coords = [(coord + direction) % 5 for coord in (letter1[0], letter2[0])]
      new_pair = ''.join([
        square[row][column] for row in new_coords
      ])
    else:
      new_pair = square[letter1[0]][letter2[1]]
      new_pair += square[letter2[0]][letter1[1]]
    ciphered.append(new_pair)
  return ''.join(ciphered).upper()

