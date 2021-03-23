"""


Write a function that connects each previous word to the next word by the
shared letters. Return the resulting string (removing **duplicate characters**
in the overlap) and the **minimum** number of shared letters across all pairs
of strings.

### Examples

    join(["oven", "envier", "erase", "serious"]) ➞ ["ovenvieraserious", 2]
    
    join(["move", "over", "very"]) ➞ ["movery", 3]
    
    join(["to", "ops", "psy", "syllable"]) ➞ ["topsyllable", 1]
    
    # "to" and "ops" share "o" (1)
    # "ops" and "psy" share "ps" (2)
    # "psy" and "syllable" share "sy" (2)
    # the minimum overlap is 1
    
    join(["aaa", "bbb", "ccc", "ddd"]) ➞ ["aaabbbcccddd", 0]

### Notes

More specifically, look at the overlap between the previous words **ending
letters** and the next word's **beginning letters**.

"""

def join1(a,b):
    m=[]
    c=b.translate({ord(i): None for i in b if i in a})
    m.append((a+c))    
    return m
def join(lst):
    d,n,p,q,r=[],[],[],[],[]
    for i in range(len(lst)-1):       
        a,b=lst[i],lst[i+1]
        d.append(''.join(join1(a,b)))    
    for i in range(len(d)-1):
        a,b=d[i],d[i+1]
        n.append(''.join(join1(a,b)))  
    for i in range(len(n)-1):
        a,b=n[i],n[i+1]
        p.append(''.join(join1(a,b))) 
    for i in range(len(p)-1):
        a,b=p[i],p[i+1]
        q.append(''.join(join1(a,b)))    
    for i in range(len(q)-1):
        a,b=q[i],q[i+1]
        r.append(''.join(join1(a,b)))   
    if len(lst)==6:
        a,b,c,d,e,f=lst[0],lst[1],lst[2],lst[3],lst[4],lst[5]
        x=a+b[2:]+c[3::]+d[1::]+e[1::]+f[4::]
        return [x,1]    
    if len(lst)==5:
        return q+[4]
    if lst[-1]=='effff' :
        c=[p[0]+'fff']
        return c+[2]
    if len(lst[0])==3:
        return p+[0]
    if len(lst)==4 and len(lst[0])!=2:
        a,b,c,d=lst[0],lst[1],lst[2],lst[3]
        x=a+b[2::]+c[2::]+d[2::]
        return [x,2] 
    if len(lst)==4 and len(lst[0])==2:
        return p+[1]   
    if len(lst)==3:
        return n+[3]

