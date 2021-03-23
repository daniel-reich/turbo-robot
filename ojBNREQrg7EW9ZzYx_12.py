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

def count_eatable_chocolates(total_money, cost_of_one_chocolate):
  try:
    x=int([i.replace('$','') for i in total_money.split() if i.replace('$','').isnumeric()][0])
    y=int([i.replace('$','') for i in cost_of_one_chocolate.split() if i.replace('$','').isnumeric()][0])
    eatable_chocolate=x//y
    wrappers=eatable_chocolate
    while not wrappers<=2:
      m=wrappers//3
      eatable_chocolate+=m
      wrappers=wrappers%3
      wrappers+=m
    return eatable_chocolate
  except:
    return 'Invalid Input'

