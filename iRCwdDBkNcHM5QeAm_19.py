"""


Write a function that takes a credit card number and only displays the last
four characters. The rest of the card number must be replaced by
`************`.

### Examples

    card_hide("1234123456785678") ➞ "************5678"
    
    card_hide("8754456321113213") ➞ "************3213"
    
    card_hide("35123413355523") ➞ "**********5523"

### Examples

  * Ensure you return a string.
  * The length of the string must remain the same as the input.

"""

def card_hide(card):
  last_num = card[-4:]
  first_num = card[:-4]
  star =""
  for n in range(len(first_num)):
    star+="*"
​
  return star+last_num

