"""


Given a number, return a string which is formatted into **US Dollars and
cents!**

Remember that:

  * You should round to two digits after the decimal point (even for integers).
  * Thousandths should be separated by commas.

### Examples

    dolla_dolla_bills(10) ➞ "$10.00"
    
    dolla_dolla_bills(1000000) ➞ "$1,000,000.00"
    
    dolla_dolla_bills(-314159.2653) ➞ "-$314,159.27"
    
    dolla_dolla_bills(-56.99) ➞ "-$56.99"

### Notes

  * There will be both negative and positive inputs.
  * Check the **Resources** Tab for many tutorials on how to approach string formatting.

"""

def dolla_dolla_bills(money):
    return '-$' + '{:,.2f}'.format(abs(money)) if money < 0 else '${:,.2f}'.format(money)

