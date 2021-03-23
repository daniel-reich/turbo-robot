"""


Create a function that takes a string and returns the reversed string. However
there's a few rules to follow in order to make the challenge interesting:

  * The UPPERCASE/lowercase positions must be kept in the same order as the original string (see example #1 and #2).
  * Spaces must be kept in the same order as the original string (see example #3).

### Examples

    special_reverse_string("Edabit") ➞ "Tibade"
    
    special_reverse_string("UPPER lower") ➞ "REWOL reppu"
    
    special_reverse_string("1 23 456") ➞ "6 54 321"

### Notes

N/A

"""

def special_reverse_string(txt):
    rev=[]
    temp=[]
    result=""
    for char in txt:
        temp.append(char)
    for i in temp:
        if i!=" ":
            rev.insert(0,i.lower())
    for j in range(len(temp)):
        if temp[j].isupper():
            rev[j]=rev[j].upper()
        if temp[j]==" ":
            rev.insert(j," ")
    for i in rev:
        result+=i
​
    return result

