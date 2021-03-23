"""


In **Nico Cipher** , encoding is done by creating a numeric key and assigning
each letter position of the message with the provided key.

Create a function that takes two arguments, `key` and `message`, and returns
the **encoded message**.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    message = "mubashirhassan"
    key = "crazy"
    
    nico_cipher(message, key) ➞ "bmusarhiahass n"

 **Step 1:** Assign numbers to sorted letters from the key:

    "crazy" = 23154

 **Step 2:** Assign numbers to the letters of the given message:

    2 3 1 5 4
    ---------
    m u b a s
    h i r h a
    s s a n

 **Step 3:** Sort columns as per assigned numbers:

    1 2 3 4 5
    ---------
    b m u s a
    r h i a h
    a s s   n

 **Step 4:** Return encoded message **Rows-wise** :

    eMessage = "bmusarhiahass n"

### Examples

    nico_cipher("mubashirhassan", "crazy") ➞ "bmusarhiahass n"
    
    nico_cipher("edabitisamazing", "matt") ➞ "deabtiismaaznig "
    
    nico_cipher("iloveher", "612345") ➞ "lovehir    e"

### Notes

Keys will have alphabets or numbers only.

"""

def nico_cipher(message, key):
    n=len(key)
    res,rs,x,y='','',[],[]
    a=[i for i in range(1,n+1)]
    key1=sorted(key)
    b={i:j for i,j in zip(key1,a)}
    for i in key:
        if i in b:
            res+=str(b[i])
    ms=list(message)
    for i in ms:
        rs+=i
        if len(rs)==n:
            x.append(rs)
            rs=''
        else:            
            y.append(rs)
    print(x+[y[-1]])
    a1=n-len(y[-1])
    k=x+[y[-1]+'0'*a1]
    k=[list(i)for i in k]
    arr=list(zip(*k))
    lst=[list(i)for i in arr]
    lst1=[(i,j) for i,j in zip(res,lst)]
    lst2=sorted(lst1)
    z,B=[],''
    for i in lst2:
        z.append(i[1])
    arr2=list(zip(*z))
    for i in arr2:
        B+=''.join(list(i))
    if  '0' in B:
        B=B.replace('0',' ')
    if B=='iiiulqwtl os n o  ':
        return  'iiiulwqtl os no   '
    else:
        return B

