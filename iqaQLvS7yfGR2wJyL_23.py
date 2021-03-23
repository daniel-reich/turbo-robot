"""


Create a function that will return an integer number containing the amount of
digits in the given integer `num`.

### Examples

    num_of_digits(1000) ➞ 4
    
    num_of_digits(12) ➞ 2
    
    num_of_digits(1305981031) ➞ 10
    
    num_of_digits(0) ➞ 1

### Notes

Try to solve this challenge without using strings!

"""

def num_of_digits(num):
    count = 0
    absolut = abs(num)
    while absolut > 0:
        absolut = absolut//10
        count += 1
    if count == 0:
        return count + 1
    else:
        return count
​
print(num_of_digits(123))

