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
# erg=[]
# for x in range(0,len(card)):
#   if (x <(len(card)-4)):
#     erg.append('*')
#   else:
#     erg.append(card[x])
# return ("".join(erg))
  s = len(card)
  return "".join(['*' if x <s-4 else card[x] for x in range(0,s)])

