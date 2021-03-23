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

def missing_alphabets(s):
    max_freq = 0
    for i in range(97, 123):
        chr_i = chr(i)
        if chr_i in s:
            freq = s.count(chr_i)
            if freq > max_freq:
                max_freq = freq
    res = ""
    for i in range(97, 123):
        chr_i = chr(i)
        if chr_i in s:
            freq = s.count(chr_i)
            res += chr_i * (max_freq - freq)
        else:
            res += chr_i * max_freq
    return res

