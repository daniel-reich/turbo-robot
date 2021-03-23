"""


In numbers theory, a positive composite integer is a Smith number if its
digital root is equal to the digital root of the sum of its prime factors,
with factors being counted by multiplicity. Trivially, every prime is also a
Smith number, having just one prime factor that is equal to itself. If two
Smith numbers are consecutive in the integer series, then they are Smith
brothers. Any other number will not be a Smith.

Given a positive integer `number`, implement a function that returns:

  * `"Youngest Smith"` if the given number is the lower element of a couple of Smith brothers.
  * `"Oldest Smith"` if the given number is the higher element of a couple of Smith brothers.
  * `"Single Smith"` if the given number is a Smith number without another Smith number adjacent, lower or higher.
  * `"Trivial Smith"` if the given number is a prime.
  * `"Not a Smith"` if the given number is not a Smith number.

### Examples

    smith_type(22) ➞ "Single Smith"
    # Digital root of 22 = 2 + 2 = 4
    # Sum of prime factors of 22 = 2 + 11 = 13
    # Digital root of 13 = 1 + 3 = 4
    # Is a Smith  number without a brother
    
    smith_type(7) ➞ "Trivial Smith"
    # The given number is a prime
    
    smith_type(728) ➞ "Youngest Smith"
    # Digital root of 728 = 7 + 2 + 8 = 17 = 1 + 7 = 8
    # Sum of prime factors of 728 = 2 + 2 + 2 + 7 + 13 = 26
    # Digital root of 26 = 2 + 6 = 8
    # The number 729 is a Smith number, so 728 is the youngest brother
    
    smith_type(6) ➞ "Not a Smith"
    # Digital root of 6 = 6
    # Sum of prime factors of 6 = 2 + 3 = 5
    # Digital root of 5 = 5

### Notes

  * The prime factors are counted by multiplicity, they don't have to be unique (see example #3).
  * Two Smith numbers are brothers if they are adjacent and if they are **composite** , a Trivial Smith (a prime) can't be the brother of a Smith number! Look at example #1: 22 is a Single Smith, despite the next one, 23 (a prime), being a Trivial Smith.
  * The digital root is the reiterated sum of the digits of a number until a single digit is reached. You can find more info in the **Resources** tab.
  * All given integers will be greater than zero.

"""

def smith_type(number):
    if smith(number) == True:
        if smith(number+1) == True:
            return("Youngest Smith")
        elif smith(number-1) == True:
            return("Oldest Smith")
        else:
            return("Single Smith")
    elif smith(number) == "Trivial Smith":
        return("Trivial Smith")
    else:
        return("Not a Smith")
    
def smith(number):
    dr_num = 9 if number%9 == 0 else number%9
    prime_nums = []
    for i in range(2, number):
        if [j for j in range(2, i) if i%j==0] == []:
            prime_nums.append(i)
    prime_factors = []
    a = number
    for x in prime_nums:
        while a%x == 0 and a > 1:
            prime_factors.append(x)
            a = a/x
    if prime_factors == [] and number != 1:
        smith = "Trivial Smith"
    elif number == 1:
        smith = "Not a Smith"
    else:
        # dr_spf refers to digit root of the sum of prime factors
        dr_spf = 9 if sum(prime_factors)%9 == 0 else sum(prime_factors)%9 
        smith = (dr_num == dr_spf)
    return(smith)

