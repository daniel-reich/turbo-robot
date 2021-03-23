"""


A **Natural Number String Sequence** is a string containing all numbers,
starting from 0, joined without spaces or other delimitators between them.

    "01234567891011121314151617181920..."

If you think of the sequence as a list, any number has a natural position
index it occupies within a string long enough to contain it based on the real
position in the numeric sequence. Looking at the example above, numbers from 0
to 9 are equals to their index position in the string; starting from 10, every
number has a string natural index position different from itself (number 10
has a position of 10|11 because it has two digits, number 11 has a position of
12|13, and so on).

When a number appears in the sequence **before** its natural position is an
**Early Bird**. Suppose that we want to know if number 12 is an Early Bird in
the above example sequence:

    01234567891011121314151617181920
    _!!___________!!________________

Natural position index of 12 is **|14, 15|** (after 11 and before 13 in the
numeric sequence), but, if we look closely at the sequence, it appears before
its natural position, at index **|1, 2|** (after 0 and before 3): 12 is then
an Early Bird number (and the first to appear, also).

You are given two integers as parameters: `_range` is the ending number of the
string sequence to generate, and `n` is the number to analyze. You must
implement a function that returns a list that contains the position indexes of
`n` (with every position index being a list in turn), and the string `"Early
Bird!"` as the last element of the list only if `n` is an Early Bird. If `n`
it's not an Early Bird and the returned list has to contain just the list with
its natural position index.

### Examples

    is_early_bird(20, 14) ➞ [[18, 19]]
    
    is_early_bird(20, 12) ➞ [[1, 2], [14, 15], "Early Bird!"]
    
    is_early_bird(101, 101) ➞ [[10, 11, 12], [193, 194, 195], "Early Bird!"]

### Notes

  * The given number `n` will be greater than 9 for every case, as trivially every single-digit number appears at the same index in the numeric sequence and in the string sequence.
  * The position indexes have to be in the order they appear in the string sequence.
  * The string at the end of the list has to be present only if `n` is an Early Bird.
  * Check the **Resources** tab for more info on this sequence.

"""

from re import finditer as find
def is_early_bird(_range, n):
    natural = sum(len(str(i)) for i in range(n-1))
    matches = find('(?=' + str(n) + ')', ''.join(map(str, range(_range +1)))) 
    indices = (match.start() for match in matches)
    ranges = [list(range(a, a + len(str(n)))) for a in indices]
    return ranges + (['Early Bird!'] if ranges[0][0] < natural else [])

