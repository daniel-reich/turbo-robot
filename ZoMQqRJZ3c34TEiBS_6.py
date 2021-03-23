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

from collections import OrderedDict
from string import punctuation
​
​
def build_polybius(keyword):
    keyword = "".join(OrderedDict.fromkeys(keyword))
    out = []
​
    row = []
    # index for ascii characters
    alplhaIndex = 97
​
    # Handle i or j in keyword
    ij = ''
    if 'i' in keyword and 'j' in keyword:
        ij = ''
    elif 'i' in keyword:
        ij = 'j'
    elif 'j' in keyword:
        ij = 'i'
​
    # Iterate until 5x5 grid is built
    i = 0
    while i < 25:
        # Add keyword character to grid until out of characters
        if i < len(keyword):
            row.append(keyword[i].lower())
        else:
            # Iterate over characters until unique character found
            char = ''
            while True:
                char = chr(alplhaIndex)
                if char in keyword + ij:
                    if alplhaIndex == 22:
                        alplhaIndex = 97
                    else:
                        alplhaIndex += 1
                else:
                    break
​
            # Group i and j into one cell
            if char == 'i':
                alplhaIndex += 2
            else:
                alplhaIndex += 1
            row.append(char)
​
        # Append row once it reaches 5 cells
        if len(row) == 5:
            out.append(row)
            row = []
​
        i += 1
​
    return out
​
​
def playfair(txt, keyword):
    if len(keyword) > 25:
        return -1
​
    # construct polybius square with keyword
    polybius = build_polybius(keyword)
​
    # print('Polybius Square: \n')
    # pprint(polybius)
    # print('')
​
    # format message to be encrypted
    message = txt.replace(' ', '').lower()
    exclude = set(punctuation)
    message = ''.join(ch for ch in message if ch not in exclude)
    message = [message[i:i+2] for i in range(0, len(message), 2)]
​
    # remove doubles from message
    for i, pair in enumerate(message):
        # If double insert x and shift all characters
        if len(pair) == 1:
            continue
        if pair[0] == pair[1]:
            oldChar = pair[1]
            message[i] = pair[0] + 'x'
​
            # iterate over all pairs to shift character
            j = i + 1
            while j < len(message):
                if(len(message[j]) == 1):
                    message[j] = oldChar + message[j]
                    oldChar = None
                else:
                    tempChar = message[j][0]
                    message[j] = oldChar + message[j][1:]
                    oldChar = message[j][1]
                    message[j] = message[j][0] + tempChar
                j += 1
​
            if oldChar != None:
                message.append(oldChar)
​
    if len(message[-1]) == 1:
        message[-1] += 'x'
​
    # print(message)
    # print('')
​
    # Set wether to encrypt of decrypt
    encrypting = True
    if not any(x in txt for x in punctuation) and not ' ' in txt and txt.isupper():
        encrypting = False
        
​
    for i, pair in enumerate(message):
        positions = []
        for char in pair:
            search = char
            if search == 'j':
                search = 'i'
​
            pos = [0, 0]
​
            # Get position of character in polybius square
            found = False
            for y, row in enumerate(polybius):
                for x, col in enumerate(row):
                    if col == search:
                        pos[0] = x
                        pos[1] = y
                        found = True
                        break
                if found:
                    break
​
            positions.append(pos)
​
        # print(positions)
​
        # If both characters are in the same row then shift them one col over
        if(positions[0][1] == positions[1][1]):
            # print('same row')
            char1 = None
            char2 = None
​
            if encrypting:
                if positions[0][0] == 4:
                    char1 = polybius[positions[0][1]][0]
                else:
                    char1 = polybius[positions[0][1]][positions[0][0] + 1]
​
                if positions[1][0] == 4:
                    char2 = polybius[positions[1][1]][0]
                else:
                    char2 = polybius[positions[1][1]][positions[1][0] + 1]
​
            else:
                if positions[0][0] == 0:
                    char1 = polybius[positions[0][1]][4]
                else:
                    char1 = polybius[positions[0][1]][positions[0][0] - 1]
​
                if positions[1][0] == 0:
                    char2 = polybius[positions[1][1]][4]
                else:
                    char2 = polybius[positions[1][1]][positions[1][0] - 1]
​
            message[i] = char1 + char2
​
        # If both characters are in the same col then shift them one row over
        elif(positions[0][0] == positions[1][0]):
            # print('same col')
            char1 = None
            char2 = None
​
            if encrypting:
                if positions[0][1] == 4:
                    char1 = polybius[0][positions[0][0]]
                else:
                    char1 = polybius[positions[0][1] + 1][positions[0][0]]
​
                if positions[1][1] == 4:
                    char2 = polybius[0][positions[1][0]]
                else:
                    char2 = polybius[positions[1][1] + 1][positions[1][0]]
            
            else:
                if positions[0][1] == 0:
                    char1 = polybius[4][positions[0][0]]
                else:
                    char1 = polybius[positions[0][1] - 1][positions[0][0]]
​
                if positions[1][1] == 0:
                    char2 = polybius[4][positions[1][0]]
                else:
                    char2 = polybius[positions[1][1] - 1][positions[1][0]]
​
            message[i] = char1 + char2
​
        # If characters are in different cols and rows form a rectangle and switch with opposite vertices
        else:
            char1 = polybius[positions[0][1]][positions[1][0]]
            char2 = polybius[positions[1][1]][positions[0][0]]
            message[i] = char1 + char2
​
    # print(''.join(message).upper())
    return ''.join(message).upper()

