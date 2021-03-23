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
    number = str(number)
    Sum = 0
    if len(number)%2 == 0: double = True
    else: double = False
    for i in range(0,len(number)):
        if double:
            addend = int(number[i])*2
            while len(str(addend))>1:
                addend = int(str(addend)[0]) +int(str(addend)[1])
            Sum+=addend
        else:
            Sum+=int(number[i])
        double= not double
    return(Sum%10 == 0)

