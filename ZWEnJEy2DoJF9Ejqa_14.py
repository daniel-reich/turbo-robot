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

def edabit_in_string(string):
    find = "edabit"
    word2make = []
    if "edabit" in string:
        return "YES"
    else:
        for j in range(len(find)):
            for i in range(len(string)):
                if string[i] == find[j]:
                    word2make.append(string[i])
                    string = string[i+1:]
                    break
        if "".join(word2make) == find:
            return "YES"
        else:
            return "NO"

