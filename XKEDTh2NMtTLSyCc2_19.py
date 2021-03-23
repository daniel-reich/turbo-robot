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
  addup=0
  lst = [int(j) for j in list(str(number))]
  lst.reverse()
  for i in range(len(lst)):
    if i % 2 !=0:
      if lst[i]*2<10:
        addup+=lst[i]*2
      else:
        addup+=sum([int(a) for a in list(str(lst[i]*2))])
    else:
      addup+=lst[i]
  if addup%10==0:
    return True
  else:
    return False

