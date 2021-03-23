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

def is_prime(x):
    for i in range(2,x-1):
        if x % i == 0:
            return False
    return True
​
def prime_factorize(num):
    temp = num
    factor_list = []
    counter = 2
    while counter <= num:
        if num % counter == 0 and is_prime(counter):
            factor_list.append(counter)
            num //= counter
            counter = 2
            continue
        counter += 1
    return factor_list

