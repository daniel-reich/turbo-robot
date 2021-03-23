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
    caps=[i for i,c in enumerate(txt) if c.isupper()]
    spaces=[i for i,c in enumerate(txt) if c==" "]
    str1="".join(txt.lower().split(" "))
    str2=str1[::-1]
    str3=""
    j=0
    for i,x in enumerate(str2):
        if j in spaces:
            j+=1
            str3=str3+" "+x
        else:
            str3=str3+x
        j+=1
    return "".join([x.upper() if i in caps else x for i,x in enumerate(str3) ])

