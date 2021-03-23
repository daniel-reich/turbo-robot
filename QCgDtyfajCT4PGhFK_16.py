"""


Write a function that returns the extended form of the prime factorization of
a number. Return in the format `[a, b, c, d, ...]`, where each element of the
list is an integer.

### Examples

    prime_factorization(216) ➞ [2, 2, 2, 3, 3, 3]
    
    prime_factorization(64) ➞ [2, 2, 2, 2, 2, 2]
    
    prime_factorization(23) ➞ [23]

### Notes

N/A

"""

def prime_factorization(number):
    temp = []
    while number % 2 == 0: 
        temp.append(2) 
        number = number // 2
          
    for i in range(3,int(number**.5)+1,2):      
        while number % i== 0: 
            temp.append(i)
            number = number // i 
              
    if number > 2: 
        temp.append(number)
    return temp

