"""


Someone is typing on the sticky keyboard. Occasionally a key gets stuck and
more than intended number of characters of a particular letter is being added
into the string. The function input contains `original` and `typed` strings.
Determine if the `typed` string has been made from the `original`. Return
`True` if it is and `False` if the typed string cannot have been made from the
`original`.

### Examples

    is_long_pressed("alex", "aaleex") ➞ True
    
    is_long_pressed("saeed", "ssaaedd") ➞ False
    
    is_long_pressed("leelee", "lleeelee") ➞ True
    
    is_long_pressed("Tokyo", "TTokkyoh") ➞ False
    
    is_long_pressed("laiden", "laiden") ➞ True

### Notes

N/A

"""

def lis(a):
    b=[]
    for i in range(len(a)):
        if a[i]!=a[i-1]:
            c=a[i]
        elif a[i]==a[i-1]:
            c+=a[i]
        if i==len(a)-1:
            b.append ( c )
        elif  a[i]!=a[i+1]:
                b.append(c)
    return b
​
​
def is_long_pressed(original, typed):
    a=lis(original)
    b=lis(typed)
    return len(a)==len(b) and all(len(a[i])<=len(b[i])for i in range(len(a)) )

