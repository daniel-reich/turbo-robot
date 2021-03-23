"""


Create a function that takes a string `txt` containing only letters from **a
to z** in lowercase and returns the **missing letter(s)** in alphabetical
order a-z.

  * A set of letters is given by `abcdefghijklmnopqrstuvwxyz`.
  * Two sets of alphabets means two or more alphabets.

### Examples

    missing_alphabets("abcdefghijklmnopqrstuvwxy") ➞ "z"
    # "z" is missing.
    
    missing_alphabets("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy") ➞ "zz"
    # Given string has a set of two alphabets so output will be "zz"
    
    missing_alphabets("edabit") ➞ "cfghjklmnopqrsuvwxyz"

### Notes

If the string contains all letters from `a-z`, return an empty string `""`.

"""

from collections import Counter
def missing_alphabets(txt):
    result = ''
    cnt_txt = Counter(txt)
    max_occurrence = max(cnt_txt.values())
    for i in range(97, 123):
        if chr(i) not in cnt_txt:
                   result += chr(i) * max_occurrence
        elif cnt_txt[chr(i)] < max_occurrence:
                   print(chr(i))
                   result += chr(i) * (max_occurrence - cnt_txt[chr(i)])
    return result

