"""


Write a function to create a Christmas tree based on height `h`.

### Examples

    tree(1) ➞ [
      "#"
    ]
    
    tree(2) ➞ [
      " # ",
      "###"
    ]
    
    tree(5) ➞ [
      "    #    ",
      "   ###   ",
      "  #####  ",
      " ####### ",
      "#########"
    ]
    
    tree(0) ➞ []

### Notes

N/A

"""

def tree(h):
    primes=[x*'#' for x in range(1,h*2) if x%2!=0]
    lst1=[]
    for x in range(1,h+1):    
        lst1.append((h-x)*(' ')+primes[x-1]+(h-x)*(' '))
    return (lst1)

