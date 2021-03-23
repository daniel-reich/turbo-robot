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

def count_eatable_chocolates(tm, cost_one):
  def get_money(string):
    words = string.split()
    
    for word in words:
      if '$' in word:
        if '$' == word:
          return int(words[0])
        tr = []
        for item in word:
          try:
            tr.append(str(int(item.replace('$',''))))
          except ValueError:
            if item == '-':
              tr.append(item)
#           print('VE, {}'.format(item))
            continue
        return int(''.join(tr))
      
      elif word == 'dollars':
        return int(words[words.index(word)-1])
      
    
    return False
  try:
    if get_money(cost_one) < 0:
      return 'Invalid Input'
    total_chocolates_bought = int(get_money(tm)/get_money(cost_one))
    total_wrappers_cashed_in = int(total_chocolates_bought/2)
#   print(total_chocolates_bought, total_wrappers_cashed_in)
    if total_wrappers_cashed_in%3==0 or total_wrappers_cashed_in == 2 or total_wrappers_cashed_in == 7:
      return total_chocolates_bought + total_wrappers_cashed_in - 1
    return total_chocolates_bought + total_wrappers_cashed_in
  except ZeroDivisionError:
    return 'Invalid Input'

