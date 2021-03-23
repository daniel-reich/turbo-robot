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

def encryption(string):
    import math
​
    # remove whitespace
    string = string.replace(' ', '')
​
    # the number of rows and cols
    # is dependent on the square
    # root of the length
    l = len(string)
    m = math.floor(math.sqrt(l))
    n = math.ceil(math.sqrt(l))
​
    # make sure the matrix is large
    # enough to hold the string
    while m * n < l:
        # always increment the
        # smaller dimension
        if m <= n:
            m += 1
​
        else:
            n += 1
​
    # create matrix of dim m x n
    matrix = [[0] * m for _ in range(n)]
​
    # add the chars into the matrix
    i = 0; j = 0
    for c in string:
        matrix[j][i] = c
​
        # update index values
        if j == n - 1:
            i += 1
            j = 0
​
        else:
            j += 1
​
    for (i, col) in enumerate(matrix):
        # remove placeholder zeros
        col = [c for c in col if c]
​
        # join rows into a string
        matrix[i] = ''.join(col)
​
    # join each col into a string
    encryptedString = ' '.join(matrix)
​
    return encryptedString

