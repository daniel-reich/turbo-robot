"""


A positive number greater than 1 can be defined untouchable when it's not
equal to the sum of the proper divisors (called also _aliquot sum_ ) of any
other positive number, in a range starting from 2 and ending with the square
of the given number (bounds included).

Given an integer `number`, implement a function that returns:

  * `True` if the given number is untouchable.
  * A list containing the numbers whose proper divisors sum is equal to the number, if the given number is not untouchable.
  * A string `"Invalid Input"` if the given number is lower than 2.

### Examples

    is_untouchable(2) ➞ True
    # Range: 2 to 4
    # 2 = 1  |  3 = 1  |  4 = 1+2 = 3
    # No sum is equal to the given number
    
    is_untouchable(3) ➞ [4]
    # Range: 2 to 9
    # As in the example above, 4 = 1+2 = 3
    
    is_untouchable(6) ➞ [6, 25]
    # Range: 2 to 36
    # 6 = 1+2+3 = 6  |  25 = 1+5 = 6
    
    is_untouchable(1) ➞ "Invalid Input"
    # The given number is lower than 2

### Notes

  * The proper divisors of a number are, merely, all its divisors less the number itself.
  * More than a number can have a proper divisors sum equal to the given number, with given number included (see example #3).
  * Trivia: As far as we know, numbers 2 and 5 are the only two primes present in the sequence, with 5 being the only odd number present; by the way, these two assertions are still unproofed.

"""

def is_untouchable(n):
    '''
    Returns True if n is not equal to the sum of the proper divisors of integers
    in the range 2 to n^2, otherwise a list of the numbers in that range whose
    sum matches it. n validated to be > 1
    '''
    if n < 2:
        return 'Invalid Input'
    
    def divisors(n):
        '''
        Returns the sum of the divisors of n
        '''
        divs = {1}
        for i in range(2, int(n**0.5) + 1):
            if not n % i:
                divs.add(i)
                divs.add(n // i)
​
        return sum(divs)
        
​
    total = [i for i in range(2, n * n + 1) if divisors(i) == n]
    return True if not total else total

