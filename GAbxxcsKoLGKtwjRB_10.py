"""


Create a function that takes a list of numbers and returns the **sum** of all
**prime numbers** in the list.

### Examples

    sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
    
    sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
    
    sum_primes([]) ➞ None

### Notes

  * Given numbers won't exceed 101.
  * A prime number is a number which has exactly two divisors.

"""

def sum_primes(list_1):
    total = 0
    if list_1 == []:
        return None
    
    if 1 in list_1:
        total -= 1
    #find primes
​
    for i in range(0, len(list_1)):
        #print(list_1[i])
        counter = 0
        for j in range(2, list_1[i]):
​
            if list_1[i] % j == 0:
                #print("NOT PRIME", list_1[i])
                counter += 1
​
        if counter == 0:
            #print("PRIME", list_1[i])
            total+= list_1[i]
​
    #print("total", total)
    return total

