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
    x = list('edabit')
    s = []
    i = 0
    while i < len(txt) and x:
        if txt[i] == x[0]:
            s += [txt[i]]
            del x[0]
        i += 1
    if ''.join(s) == 'edabit':
        return 'YES'
    else:
        return 'NO'

