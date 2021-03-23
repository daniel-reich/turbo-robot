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
  num_list = [int(i) for i in str(number)][::-1]
  num_list2 = [num_list[i]*2 if i%2 == 1 else num_list[i] for i in range(len(num_list))]
  num_list3 = [int(str(i)[0]) + int(str(i)[1]) if i > 9 else i for i in num_list2]
  return sum(num_list3)%10 == 0

