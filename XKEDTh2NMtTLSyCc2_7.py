"""


Create a function that takes a number and checks whethers the given number is
a valid credit card number using **Luhn Algorithm**. The return value is
boolean.

### Examples

    valid_credit_card(4111111111111111) ➞ True
    # Visa Card
    
    valid_credit_card(6451623895684318) ➞ False
    # Not a valid credit card number.
    
    valid_credit_card(6451623895684318) ➞ False

### Notes

  * American Express/VISA/Discover/Diner Club may be the credit card type.
  * Check the **Resources** for help.

"""

def valid_credit_card(number):
    s = str(number)
    sum1 = sum([f(s[i]) for i in range(len(s)-2,-1,-2)])
    sum2 = sum([int(s[i]) for i in range(len(s)-3,-1,-2)])
    return 9 * (sum1 + sum2) % 10 == int(s[-1])
          
def f(s):
    x = 2*int(s)
    if x > 9:
        x = x-9
    return x

