"""


Create a function thats takes a list and returns `True` if every number is
prime. Otherwise, return `False`.

### Examples

    all_prime([7, 5, 2, 4, 6]) ➞ False
    
    all_prime([2, 3, 5, 7, 13, 17, 19, 23, 29]) ➞ True
    
    all_prime([1, 5, 3]) ➞ False

### Notes

1 is not a prime number.

"""

#edabit
#list of prime numbers
​
def all_prime(lst):
    result = True
    for num in lst:
        if num == 1:
            result = False
            break
        else:
            for i in range(2,num):
                if num % i == 0:
                    result = False
                    break
    return result
​
def main():
    pass
​
if __name__ == "__main__":
    main()

