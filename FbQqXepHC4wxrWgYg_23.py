"""


Given a number, return all its prime divisors in a list. Create a function
that takes a number as an argument and returns all its prime divisors.

  * n = 27
  * All divisors: `[3, 9, 27]`
  * Finally, from that list of divisors, return the prime ones: `[3]`

### Examples

    prime_divisors(27) ➞ [3]
    
    prime_divisors(99) ➞ [3, 11]
    
    prime_divisors(3457) ➞ [3457]

### Notes

N/A

"""

def prime_divisors(num):
    count=0
    lst=[]
    for i in range(2,num+1):
        if num %i ==0:
            for j in range(2,i):
                if i % j == 0:
                    count+=1
            if count == 0:
                lst.append(i)
        count=0
    return lst

