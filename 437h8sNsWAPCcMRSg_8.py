"""


Write a function that returns `True` if the given number `num` is a product of
any two prime numbers.

### Examples

    product_of_primes(2059) ➞ True
    # 29*71=2059
    
    product_of_primes(10) ➞ True
    # 2*5=10
    
    product_of_primes(25) ➞ True
    # 5*5=25
    
    product_of_primes(999) ➞ False
    # There are no prime numbers.

### Notes

  * `num` is always greater than 0.
  * `0` and `1` aren't prime numbers.

"""

def product_of_primes(num):
    arrFactor = []
    arrMulti = []
    multiplier = 2
    while num != 1:
        if divmod(num,multiplier)[1] == 0:
            if multiplier in arrFactor:
                arrMulti[len(arrMulti)-1] += 1
            else:
                arrFactor.append(multiplier)
                arrMulti.append(1)
            num = num / multiplier
        else:
            multiplier += 1
​
​
​
    if len(arrFactor) == 1 and arrMulti[0] == 2:
        return True
    elif len(arrFactor) == 2:
        if arrMulti[0] == 1 and arrMulti[1] == 1:
            return True
        else:
            return False
    else:
        return False

