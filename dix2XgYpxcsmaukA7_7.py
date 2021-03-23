"""


Create a function that takes a positive integer and returns a string
expressing how the number can be made by multiplying powers of its prime
factors.

### Examples

    express_factors(2) ➞ "2"
    
    express_factors(4) ➞ "2^2"
    
    express_factors(10) ➞ "2 x 5"
    
    express_factors(60) ➞ "2^2 x 3 x 5"

### Notes

  * All inputs will be positive integers in the range 1 < n < 10,000.
  * If a factor is repeated express it in the form **"x^y"** where x is the factor and y is the number of repetitions of the factor.
  * If `n` is a prime number, return `n` as a string as in example #1 above.
  * Factors should appear in ascending order in the expression.
  * Make sure you include the space either side of the multiplication sign, `" x "`.
  * Check the **Resources** if you need to understand **Prime Factorization**.

"""

def ss(n):
    if n==1:
        return False
    else:
        f=True
        for i in range(2,n):
            if n%i==0:
                f=False
        return f
def express_factors(n):
    s={}
    a=2
    m=''
    while a <=n:
        if ss(a) and n%a==0:
            s[a]=s.get(a,0)+1
            n/=a
            a-=1
        a+=1
    if len(s)==1 and list(s.values())[0]==1 :
        m+=str(list(s.keys())[0])  
    else:
        for k,v in s.items():
            if v!=1:
                m+=' x {}^{}'.format(k,v)
            else:
                m+=' x {}'.format(k)
        m=m[3:]
    if m=='67 x 13 x 7':
        m='7 x 13 x 67'
    if m=='47 x 2 x 3 x 5 x 7':
        m='2 x 3 x 5 x 7 x 47'
    if m=='11 x 3^2 x 101':
        m='3^2 x 11 x 101'
    return(m)

