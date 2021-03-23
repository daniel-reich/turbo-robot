"""


The Japanese _soroban_ is type of abacus (counting tool) that is used by
sliding threaded beads up and down wires. The soroban is divided into an upper
deck (where each bead is worth 5 units) and a lower deck (where beads are
worth 1 unit). Working from the right and moving to the left, units increase
by a factor of 10. If we use "O" for a bead and "|" to show the wire, we can
represent the soroban as follows:

    OOOOOOO
    |||||||  Upper deck
    -------  Dividing line
    |||||||  Lower deck
    OOOOOOO
    OOOOOOO
    OOOOOOO
    OOOOOOO

To read the number, we count the value of the number of beads that have been
moved _towards_ the dividing line. The values for the upper and lower deck are
added together. In the example below, the number is **30651** :

    OOOO||O
    ||||OO|
    -------
    ||O|O|O
    OOOO|O|
    OOOOOOO
    OO|OOOO
    OOOOOOO
    
    0000550  Upper deck
    0030101  Lower deck
      30651  Total

Given a list of strings representing the soroban, return the _number_ being
displayed.

### Examples

    soroban([
      "OOOO||O",
      "||||OO|",
      "-------",
      "|||O|OO",
      "OOOOOOO",
      "OOO|OOO",
      "OOOOO|O",
      "OOOOOO|"
    ]) ➞ 2584
    
    soroban([
      "||OO||O",
      "OO||OO|",
      "-------",
      "OO|OO||",
      "OOO|OOO",
      "OOOO|OO",
      "|OOOOOO",
      "O|OOOOO"
    ]) ➞ 8901750

### Notes

For more info on how to use a soroban, please check the **Resources** tab.

"""

def soroban(frame):
  global_count = 0
  for i in range(0,7):
    count = 0
    if frame[0][i] == "|":
      count += 5
    n=3
    while frame[n][i].lower() == 'o':
      count +=1
      n+=1
  
    global_count += 10**(6-i)*count
  
  return global_count

