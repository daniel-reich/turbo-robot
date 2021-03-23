"""


Write a function that receives a list of words and a mask. Return a list of
words, sorted alphabetically, that match the given mask.

### Examples

    scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “*re**”) ➞ [“creed”]
    
    scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “***”) ➞ [“dee”, “ree”]

### Notes

The length of a mask will never exceed the length of the longest word in the
word list.

"""

def scrambled(words, mask):
    a=len(mask)
    x,y,z,m=[],[],[],[]
    for i,v in enumerate(mask):
        if v.isalpha():
            y.append(v)
    for i,v in enumerate(words):
        if len(v)==a :
            x.append(v)
    res=''
    for k in x:
        b=([i+j for i,j in zip(k,mask)])
        for i in b:
            if len(set(i))==1 and '*' not in i:
                   res+=i[0]
        z.append(res)
        res=''
    c=[[i,j]for i,j in zip(x,z)]
    for i in c:
        if len(i[1])==len(y):
            m.append(i[0])
    return m

