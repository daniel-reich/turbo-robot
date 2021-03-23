"""


A string contains the word "edabit" if a _subsequence_ of its characters spell
"edabit".

Write a function that accepts a string and returns “YES” if the string
contains a subsequence of the word edabit or "NO" if it does not.

### Examples

    edabit_in_string(“eddaaabt”) ➞ “NO”
    
    edabit_in_string(“edwardisabletodoit”) ➞ “YES”
    
    edabit_in_string(“abecdfghijklmnopqrstuvwxyz”) ➞ “NO”

### Notes

Check the **Resources** tab for more details on subsequence.

"""

def edabit_in_string(txt):
    test = 'edabit'
    res = ''
    idx_start = -1
    for c in test:
        idx_start = txt.find(c, idx_start+1)
        if idx_start > -1:
            res += c
        else:
            break
            
    return 'YES' if test == res else 'NO'

