"""


Make a function that returns `True` if an integer is prime or `False` if the
number is composite. All test cases are of very large numbers, so **trial
division won't cut it**.

### Examples

    is_prime(308860934436978480666476812207644303437) ➞ True
    # The only factors for this number are 1 and itself.
    
    is_prime(27464981106643782905056206820270083251) ➞ False
    # This equals 13803066116705972713 * 1989773929533140027
    
    is_prime(12930519935023769075526485657382658729) ➞ False
    # This is 3595903215469483277 squared

### Notes

See the **Resources** tab for some great explanations of how computers can
find very large prime numbers for cryptography applications.

"""

import random
def is_prime(number):
    # if number != 1
    if (number > 1):
        # repeat the test few times
        for _ in range(3):
            # Draw a RANDOM number in range of number ( Z_number )  
            randomNumber = random.randint(2, number)-1
            
            # Test if a^(n-1) = 1 mod n 
            if ( pow(randomNumber, number-1, number) != 1 ):
                return False
        
        return True
    else:
        # case number == 1
        return False

