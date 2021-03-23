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

def digits(n):
    return [int(i)for i in str(n)]
def valid_credit_card(number):
    x=digits(number)
    y=x[-1::-2]
    z=x[-2::-2]
    count=0
    count+=sum(y)
    for i in z:
        count+=sum(digits(i*2))
    a=count%10
    print(a)
    return a==0

