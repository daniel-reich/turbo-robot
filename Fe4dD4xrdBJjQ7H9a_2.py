"""


 _Backpack Bill and Wallet Will set off for the annual festival. As they
approach the stalls, Bill retorts that he'll be able to bring home more stuff
than Will. Taking this as a challenge, Will refutes and a competition spurs
into action._

  * Backpack Bill has an infinite inventory space, but a limited number of coins.
  * Wallet Will has an infinite number of coins, but a limited inventory space.

 **Create a function that returns the name of the man who can bring home the
most items. The parameters are given as follows:**

  1. Bill's amount of money.
  2. Will's amount of inventory space.
  3. The item's price.
  4. The item's size.

### Worked Example

    who_wins_tonight(40, 95, 5, 10) ➞ "Will"
    
    # The item costs 5 coins and takes up 10 inventory spaces.
    # Bill can only buy a maximum of 8 items (40 coins DIV 5 = 8).
    # Will can only bring home a maximum of 9 items. (95 inventory spaces DIV 10 = 9).
    # Will is the winner.

### Examples

    who_wins_tonight(20, 20, 5, 10) ➞ "Bill"
    
    who_wins_tonight(10, 2, 20, 1) ➞ "Will"
    
    who_wins_tonight(3, 7, 2, 5) ➞ "Tie"

### Notes

  * DIV means a floored division. That means you round down after dividing.
  * Return `"Tie"` if both men can afford the same amount of stuff.
  * All numbers will be positive integers.

"""

who_wins_tonight = lambda c,s,p,z:'Tie' if c//p == s//z else'Bill' if c//p > s//z else 'Will'

