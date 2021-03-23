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
    text=list(str(number))
​
    for i in range(len(text)-2,-1,-2):
        t=int(text[i])*2
        if(t>9):
            t=t-9
        text[i]=t
    sum=0
    for i in range(len(text)):
        sum=sum+int(text[i])
​
​
    if(sum%10==0):
        return True
    else:
        return False

