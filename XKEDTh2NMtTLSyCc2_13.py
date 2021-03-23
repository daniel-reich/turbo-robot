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
    a,b=[],[]
    for i in str(number)[-2::-2]:
        a.append(int(i)*2)
    for i in range(len(a)):
        if a[i] > 9:
            a[i]=int(str(a[i])[0])+int(str(a[i])[1])
    for i in str(number)[::-2]:
        b.append(int(i))
    if (sum(a)+sum(b))%10==0:
        return True
    else:
        return False

