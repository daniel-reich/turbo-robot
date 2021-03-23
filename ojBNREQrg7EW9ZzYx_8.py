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

def count_eatable_chocolates(t, c):
  t = int(''.join([i for i in t if i.isdigit() or i=='-']))
  c = int(''.join([i for i in c if i.isdigit() or i=='-']))
  if t<=0 or c<=0:
    return 'Invalid Input'
  w = 0
  tot = 0
  while w>=3 or t>=c:
    if w>=3:
      w-=2
      tot+=1
    elif t>=c:
      t-=c
      w+=1
      tot+=1
  return tot

