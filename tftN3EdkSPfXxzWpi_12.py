"""


Create a function that returns the sentence that contains the word at index
`n`. Remember to include the full stop at the end.

### Worked Example

    txt = "I have a dog. I have a log. There is no stopping me now."
    
    sentence_searcher(txt, 7) ➞ "I have a log."
    # The word at index 7 is "log".
    # The full sentence that contains the word at index 7 is "I have a log."
    # Return the sentence.

### Examples

    sentence_searcher(txt, 2) ➞ "I have a dog."
    
    sentence_searcher(txt, 4) ➞ "I have a log."
    
    sentence_searcher(txt, -1) ➞ "There is no stopping me now."
    # The index at -1 is the last word.
    # The last word is "now".

### Notes

  * All sentences will end with a full stop.
  * You need to also account for negative indexes.

"""

def sentence_searcher(txt, n):
    txt2=txt[::-1].split('.')
    lst=[i[::-1].split()for i in txt2[1::]]
    txt=txt.split('.')
    lst2=[i.split()for i in txt]
    x,y,p,k=[],[],[],[]
    for j,i in enumerate(txt):
        a=len(i.split())
        x.append(a)
    b=(x[1],x[1]+x[0])
    c=(x[1]+x[0],x[2]+x[1]+x[0])
    y.append((0,x[0]))
    y.append(b)
    y.append(c)
    s,t,r,u=[],[],[],[]
    s.append([-i for i in range(1,len(lst[0])+1)])
    s.append([-i for i in range(len(lst[0])+1,len(lst[1])+len(lst[0])+1)])
    s.append([-i for i in range(len(lst[1])+len(lst[0])+1,len(lst[2])+len(lst[1])+len(lst[0])+1)])
    for i in y:
        for j in range(i[0],i[1]):
             p.append(j)
        k.append(p)
        p=[] 
    lst1=[[i,j]for i,j in zip(s,lst)]
    lst3=[[i,j]for i,j in zip(k,lst2)]
    if n>=0:
        for i in lst3:
            if n in i[0]:
                return ' '.join(i[1])+'.'          
    else:  
        for i in lst1:
            if n in i[0]:
                return ' '.join(i[1])+'.'

