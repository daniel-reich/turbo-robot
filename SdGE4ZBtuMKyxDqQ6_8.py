"""


Create a function that takes a string and returns the first character that
repeats. If there is no repeat of a character, then return "-1".

### Examples

    first_repeat("legolas") ➞ "l"
    
    first_repeat("Gandalf") ➞ "a"
    
    first_repeat("Balrog") ➞ "-1"
    
    first_repeat("Isildur") ➞ "-1"

### Notes

Tests are case sensitive.

"""

def first_repeat(chars):
    tstring=chars
    getlen=len(tstring)
    if (getlen%2)==0:
        fac=int(getlen/2)
    else:
        fac=int((getlen+1)/2)
    
    fstr=tstring[:fac]
    sstr=tstring[fac:]
    for k,i in enumerate(fstr):
        ind=fstr.index(i)
        if i in sstr or i in fstr[ind+1:]:
            #ind=sstr.index(i)
            #print('{} is repeated at index {}'.format(i,ind+fac))
            return i
            break
        elif (k==len(fstr)-1):
             return '-1'

