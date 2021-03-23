"""


A number is Economical if the quantity of digits of its prime factorization
(including exponents greater than 1) is equal to or lower than the digit
quantity of the number itself.

Given an integer `n`, implement a function that returns a string:

  * `"Equidigital"` if the quantity of digits of the prime factorization (including exponents greater than 1) is equal to the quantity of digits of `n`;
  * `"Frugal"` if the quantity of digits of the prime factorization (including exponents greater than 1) is lower than the quantity of digits of `n`;
  * `"Wasteful"` if none of the two above conditions is true.

### Examples

    is_economical(14) ➞ "Equidigital"
    # The prime factorization of 14 (2 digits) is [2, 7] (2 digits)
    # Exponents equal to 1 are not counted
    
    is_economical(125) ➞ "Frugal"
    # The prime factorization of 125 (3 digits) is [5^3] (2 digits)
    # Notice how exponents greater than 1 are counted
    
    is_economical(1024) ➞ "Frugal"
    # The prime factorization of 1024 (4 digits) is [2^10] (3 digits)
    
    is_economical(30) ➞ "Wasteful"
    # The prime factorization of 30 (2 digits) is [2, 3, 5] (3 digits)

### Notes

  * Any given `n` will be a positive integer greater than 1.
  * Remember to count also the exponents greater than 1 into the prime factorization: 2¹ = 2 (one digit), 2² = 22 (two digits), 2¹° = 210 (three digits)...

"""

from collections import Counter
​
import math as mt 
  
MAXN = 100001
  
​
spf = [0 for i in range(MAXN)]
​
def sieve(): 
    spf[1] = 1
    for i in range(2, MAXN): 
          
       
        spf[i] = i 
  
    # separately marking spf for  
    # every even number as 2 
    for i in range(4, MAXN, 2): 
        spf[i] = 2
  
    for i in range(3, mt.ceil(mt.sqrt(MAXN))): 
          
     
        if (spf[i] == i): 
              
         
            for j in range(i * i, MAXN, i):  
            
                if (spf[j] == j): 
                    spf[j] = i 
​
def getFactorization(x): 
    ret = list() 
    while (x != 1): 
        ret.append(spf[x]) 
        x = x // spf[x] 
  
    return ret 
​
def is_economical(n):
    h=[]
    sieve()
    
    p=getFactorization(n)
    s=digit(n)
    d=Counter(p)
    print(d)
    
    rr=""
    for c,e in d.items():
        
        if e>1:
            rr+=str(c)+str(e)
        else:
            rr+=str(c)
    print(rr)
  
    m=len(rr)
    
    
    if m==s:
        return "Equidigital"
    elif m<s:
        return "Frugal"
    else:
        return "Wasteful"
            
    
def digit(n):
    q=str(n)
    d=[]
    for i in q:
        d.append(q)
    return len(d)

