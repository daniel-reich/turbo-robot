"""


Arun recently started eating chocolates. The shopkeeper tells Arun that for
every three chocolates Arun eats, he will give him one chocolate in exchange
for three chocolate wrappers. Now, Arun is confused about how many chocolates
he can eat.

Given the `total_money` Arun has and the `cost_of_one_chocolate`, help him
figure out how many chocolates he can eat.

### Examples

    count_eatable_chocolates("4$", "1$") ➞ 5
    # Arun eats three chocolates and purchases one more
    # chocolate from Bitu in those three wrappers. Now he
    # eats those two chocolates and hence 3 + 2 = 5.
    
    count_eatable_chocolates("55   $", "5$") ➞ 16
    
    count_eatable_chocolates("I have 68$", "2$")  ➞ 50
    
    count_eatable_chocolates("I got -68$ from my mom ", "2$")  ➞ "Invalid Input"
    # Because -68 is a negative number and money can't be negative.

### Notes

Figure out the invalid inputs and take care of them.

"""

import re
def count_eatable_chocolates(txt, price):
    rx = re.compile(r'(?<!-)\b\d+(?=\s*(?:[$]|dollars))')
    m, p = rx.findall(txt), rx.findall(price)
    if not m or not p or p[0] == '0': return "Invalid Input"
    count = wrappers = int(m[0]) // int(p[0])
    while wrappers >= 3:
        chocs, wrappers = divmod(wrappers, 3)
        count += chocs
        wrappers += chocs
    return count

