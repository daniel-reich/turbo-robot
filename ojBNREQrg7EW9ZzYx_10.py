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

def count_eatable_chocolates(money_, cost_):
    money, cost = "", ""
    for i in money_:
        if i.isnumeric():
            money += i
    p_1 = money_.find(money)
    if p_1 > 0 and money_[p_1-1] == "-" or int(money) <= 0:
        return "Invalid Input"
    money = int(money)
    for i in cost_:
        if i.isnumeric():
            cost += i
    p_2 = cost_.find(cost)
    if p_2 > 0 and cost_[p_2-1] == "-" or int(money) <= 0:
        return "Invalid Input"
    cost = int(cost)
    poop, stock =  0, 0
    while money >= cost:
        eat = money // cost
        poop += eat
        wrappers = eat + stock
        money = money - eat * cost + wrappers // 3 * cost
        stock = wrappers % 3
    return poop

