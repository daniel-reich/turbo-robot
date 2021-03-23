"""


Write a function to find all the prime factors of a given integer. The
function must return a list containing all the prime factors, sorted in
ascending order. Remember that _1 is neither prime nor composite_ and should
not be included in your output list.

### Examples

    prime_factorize(25) ➞ [5, 5]
    
    prime_factorize(19) ➞ [19]
    
    prime_factorize(77) ➞ [7, 11]

### Notes

  * Output list must be sorted in ascending order.
  * The only positive integer which is neither prime nor composite is 1. Return an empty list if 1 is the input.

"""

def prime(n):
    l = []
    for i in range(n+1):
        for j in range(n+1):
            if i*j == n:
                l.append(i)
​
    return len(l)
​
def prime_factorize(num):
    l = []
    l2 = []
    for i in range(2,num+1):
        for j in range(num+1):
            if i*j == num:
                l.append(i)
    l.sort()
    for i in l:
        if prime(i) ==2:
            h = 1
            for x in range(num):
                h = h*i
                if h in l:
                 l2.append(i)
​
    return l2
print( prime_factorize(2532))

