"""


An English text needs to be encrypted using Edabit’s encryption scheme. First,
the spaces are removed from the text. Let _L_ be the length of this text.
Then, characters are written into a grid, whose rows and columns have the
following constraints:

For example, the sentence " _if man was meant to stay on the ground god would
have given us roots_ ", after removing spaces, is _54_ characters long. The
square root of 54 is between 7 and 8, so it is written in the form of a grid
with 7 rows and 8 columns.

    ifmanwas
    meanttos
    tayonthe
    groundgo
    dwouldha
    vegivenu
    sroots

  * Ensure that _rows x column >= L_
  * If multiple grids satisfy the above conditions, choose the one with the minimum area.

    rows x columns >= L

The encoded message is obtained by displaying the characters in a column,
inserting a space, and then displaying the next column and inserting a space,
and so on. For example, the encoded message for the above rectangle is:

    imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

### Examples

    encryption(“haveaniceday”) ➞ “hae and via ecy”
    
    # have
    # anic
    # eday
    
    encryption(“feedthedog”) ➞ “fto ehg ee dd”
    
    encryption(“chillout”) ➞ “clu hlt io”
    
    encryption(“A Fool and His Money Are Soon Parted.”) ➞ "Anoea FdnSr oHeot oiyoe lsAnd aMrP."

### Notes

  * Ensure capitalization remains the same in encrypted text.
  * Do not remove special characters.

"""

import math
​
def encryption(txt: str) -> str:
    txt = ''.join(txt.split())
    rows, cols = math.floor(math.sqrt(len(txt))), math.ceil(math.sqrt(len(txt)))
    if rows * cols < len(txt):
        rows += 1
    L = [txt[cols * i: cols *(i+1)] for i in range(rows)]
    K = [i if len(i) == len(L[0]) else i + ' ' * (len(L[0]) - len(i)) for i in L]
    return ' '.join(''.join(i).rstrip() for i in zip(*K))

