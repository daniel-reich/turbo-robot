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
    x="abcdefghijklmnopqrstuvwxyz"
    res=''
    if len(x)==len(txt):
        return ""
    b=txt.count(txt[1])
    if b==1:
        for i in x:
            if i not in txt:
                res+=i
        return res        
    else:
        rs=''
        for i in x:
            c=txt.count(i)
            if c>1 and i not in rs:
                rs+=i*c
            else:
                res+=i*c
                if i not in res:
                    res+=i*b
        return res

