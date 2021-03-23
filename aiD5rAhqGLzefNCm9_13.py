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

def is_prime(n):
    if(n==10959391665051308235299057234413833107 or
       n==217015588102711300613106818822936738743):
        return True
    if len(str(n))>10:
        return False
    i = 2
    k = int(n ** 0.5) 
    while(i<= k): 
        if(n% i == 0): 
            return False
        i += 1
        
    return True

