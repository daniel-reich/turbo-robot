"""


Two players draw a pair of numbered cards so that both players can form a _2
digit number_. A winner can be decided if one player's number is larger than
the others.

However, there is a rule where a player can swap any one of their cards with
any one of the other player's cards in a gamble to get a higher number! Note
that it is illegal to swap the order of **your own cards**. That means if you
draw a `1` then a `9`, you **cannot** swap them to get `91`.

![Numbered Cards](https://edabit-challenges.s3.amazonaws.com/ffnIjMHhwK.png)

Paul's strategy is to always swap his **lowest** number with the opponent's
**ten's digit**. Return whether this results in Paul winning the round.

  * `n1` is Paul's number
  * `n2` is his opponent's number

### Worked Example

    swap_cards(41, 79) ➞ True
    # Paul's lowest number is 1
    # The opponent's ten's digit is 7
    # After the swap: 47 > 19
    # Paul wins the round

### Examples

    swap_cards(41, 98) ➞ True
    
    swap_cards(12, 28) ➞ True
    
    swap_cards(67, 53) ➞ False
    
    swap_cards(77, 54) ➞ False

### Notes

  * If both of Paul's digits are the same, swap the ten's digit with the opponent's (paul likes to live riskily).
  * The cards don't include the number **0**.

"""

def swap_cards(n1, n2):
  low=min([int(i) for i in str(n1)])
  opp=str(low)+str(n2)[1]
  paul=[str(n1)[0],str(n1)[1]]
  paul.remove(str(low))
  paul.append(str(n2)[0])
  
  pscore=''
  if paul[0]==str(n1)[0]:
    pscore=paul[0]+paul[1]
  else:
    pscore=paul[1]+paul[0]
    
  if str(n1)[0]==str(n1)[1]:
    pscore=int(str(pscore)[::-1])
    return int(pscore)>int(opp)
  else:
    return int(pscore)>int(opp)

