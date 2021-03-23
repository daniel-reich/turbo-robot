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
    char_map=[]
    for char in txt:
        if char==" ":
            char_map.append('S')
        elif char.isalpha():
            if char.islower():
                char_map.append('L')
            else:
                char_map.append('U')
        elif char.isdigit():
            char_map.append('N')
        else:
            char_map.append('L')
​
​
    txt2=txt.replace(" ","").lower()[::-1]
​
    result=""
    j=0
    for i in range(0,len(txt)):
        if char_map[i]=='S':
            result+=" "
        if char_map[i]in ('L','N'):
            result += txt2[j]
            j+=1
        if char_map[i] == 'U':
            result += txt2[j].upper()
            j+=1
​
    return result

