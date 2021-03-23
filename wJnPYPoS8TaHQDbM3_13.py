"""


Las Vegas style dice have 6 sides numbered 1 to 6. When rolling 2 dice, a six
is 5 times more likely than a two because a six can be rolled 5 different ways
(1 + 5, 5 + 1, 2 + 4, 4 + 2, 3 + 3), while a two can only be rolled 1 way (1 +
1).

Create a function that accepts two arguments:the number of dice rolled, and
the outcome of the roll. The function returns the number of possible
combinations that could produce that outcome. The number of dice can vary from
1 to 6.

For the example given above:

  * `dice_roll(2, 6)` would return `5`
  * `dice_roll(2, 2)` would return `1`

### Examples

    dice_roll(1, 3) ➞ 1
    
    dice_roll(2, 5) ➞ 4
    # 1 + 4, 4 + 1, 2 + 3, 3 + 2
    
    dice_roll(3, 4) ➞ 3
    # 1 + 1 + 2, 1 + 2 + 1, 2 + 1 + 1
    
    dice_roll(4, 18) ➞ 80
    
    dice_roll(6, 20) ➞ 4221

### Notes

1 + 5 and 5 + 1 are distinct combinations because die #1 can show 1 while die
#2 can show 5, or die #1 can show 5 while die #2 can show 1.

"""

def convert10_to_base(n, base):
    result, extra_digits = '', 'ABCDEF'
    while n > 0:
        remainder = n % base
        if remainder < 10:
            result += str(remainder)
        else:
            result += extra_digits[remainder - 10]
        n = n // base
    return result[::-1]
​
​
def make_dices_combination(num, n_digits):
    res = n_digits * [1]
    s = convert10_to_base(num, 6)
    for j in range(1, min(len(s), len(res)) + 1):
        res[-j] += int(s[-j])
    return res
​
​
def dice_roll(n, outcome):
    count = 0
    for i in range(6 ** n):
        if sum(make_dices_combination(i, n)) == outcome:
            count += 1
    return count

