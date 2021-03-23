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

def missing_alphabets(txt):
    r, m = [], 0
    alpha = "abcdefghijklmnopqrstuvwxyz"
    dic = dict.fromkeys(alpha, 0)
    for i in alpha:
        current = txt.count(i)
        m = max(m, current)
        dic[i] = current
    for j in dic.items():
        if j[1] < m:
            add = (m - j[1]) * j[0]
            r.append(add)
    return "".join(sorted(r))

