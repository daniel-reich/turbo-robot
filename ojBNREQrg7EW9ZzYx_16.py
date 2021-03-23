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
  a = ['-','1','2','3','4','5','6','7','8','9','0']
  
  tot = ''
  total_money = list(total_money)
  for i in total_money:
    if i in a:
      tot += i
  cost = ''
  cost_of_one_chocolate = list(cost_of_one_chocolate)
  for i in cost_of_one_chocolate:
    if i in a:
      cost += i
  tot = int(tot)
  cost = int(cost)
  if tot < 1:
    return 'Invalid Input'
  elif cost < 1:
    return 'Invalid Input'
  ctr = tot // cost
  pur = tot // cost
  wrap = pur
  
  while wrap >= 3:
    pur = wrap // 3
    wrap = pur + wrap % 3
    ctr += pur
    
    
  return ctr

