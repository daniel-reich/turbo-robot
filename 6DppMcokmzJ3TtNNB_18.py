"""


Create a function which takes every letter in every word, and puts it in
alphabetical order. Note how the **original word lengths must stay the same**.

### Examples

    true_alphabetic("hello world") ➞ "dehll loorw"
    
    true_alphabetic("edabit is awesome") ➞ "aabdee ei imosstw"
    
    true_alphabetic("have a nice day") ➞ "aaac d eehi nvy"

### Notes

  * All sentences will be in lowercase.
  * No punctuation or numbers will be included in the **Tests**.

"""

def true_alphabetic(txt):
    s = ''
    for x in txt:
        if x != ' ':
            s += x
    s = sorted(s)
    ans = ''
    j = 0
    for x in txt:
        if x == ' ':
            ans += x
        else:
            ans += s[j]
            j += 1
    return ans

