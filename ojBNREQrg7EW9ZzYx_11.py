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
​
​
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
    total_money = int(re.findall(r'-?\d+', total_money)[0])
    cost_of_one_chocolate = int(re.findall(r'-?\d+', cost_of_one_chocolate)[0])
    if cost_of_one_chocolate <= 0 or total_money < 0:
        return 'Invalid Input'
    current_eatable_chocolates = total_money // cost_of_one_chocolate
    total_eatable_chocolates = 0
​
    while current_eatable_chocolates > 0:
​
        if current_eatable_chocolates >= 3:
            current_eatable_chocolates -= 3
            total_eatable_chocolates += 3
            current_eatable_chocolates += 1
​
        else:
            total_eatable_chocolates += current_eatable_chocolates
            break
​
    return total_eatable_chocolates

