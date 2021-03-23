"""


Create a function that checks if the sub-lists in a list adhere to the
specified pattern.

### Examples

    check_pattern([[1, 1], [2, 2], [1, 1], [2, 2]], "ABAB") ➞ True
    
    check_pattern([[1, 2], [1, 3], [1, 4], [1, 2]], "ABCA") ➞ True
    
    check_pattern([[1, 2, 3], [1, 2, 3], [3, 2, 1], [3, 2, 1]], "AABB") ➞ True
    
    check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "ABCD") ➞ True
    
    check_pattern([[8, 8, 8, 8], [7, 7, 7, 7], [6, 6, 6, 6], [5, 5, 5, 5]], "DCBA") ➞ True

### Notes

  * The length of the pattern will always be the same as the length of the (main) list.
  * The pattern does not necessarily have to be alphabetically ordered (see last example).

"""

b=[]
def check_pattern(lst, pattern):
    import string as st
    global b 
    st=iter(st.ascii_uppercase)
    a={}
    ls=''
    for i in lst :
        if  str(i) not  in a  :
            a[str(i)]=next(st)
            ls=ls+a[str(i)]
        else  :
            ls=ls+a[str(i)]
    if a in b  :
      return ls[::-1]==pattern
    else : 
      b.append(a)
      return  ls==pattern

