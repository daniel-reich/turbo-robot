"""


Given a lottery ticket (`ticket`), represented by a list of 2-value lists,
create a function to find out if you've won the jackpot.

To do this, you must first count the 'mini-wins' on your `ticket`. Each
sublist has both a string and a number within it. If the character code of any
of the characters in the string matches the number, you get a mini-win. Note
you can only have one mini-win per sublist.

Once you have counted all of your mini-wins, compare that number to the other
input provided (`win`). If your number of mini-wins is more than or equal to
`win`, return `Winner!`. Else, return `Loser!`.

### Examples

    lottery([["YYW", 70], ["WXK", 65], ["RPDI", 88]], 2)
    ➞ "Loser!"
    
    lottery([["KG", 80], ["NTBBVZ", 79], ["CI", 73], ["AGXMEE", 74], ["IU", 68], ["VOSP" , 84]], 1)
    ➞ "Winner!"
    
    lottery([["ZSAMZB", 81], ["XWWCXP", 72], ["SYBRQOHP", 88], ["HJSVV", 75]], 1)
    ➞ "Loser!"

### Notes

  * All inputs will be in the correct format.
  * Strings on `ticket` are not always the same length.

"""

def lottery(ticket, win):
  miniwin=0
  for i in range(0,len(ticket)):
    for z in range(0,len(ticket[i][0])):
      if(ord(ticket[i][0][z])==ticket[i][1]):
        miniwin=miniwin+1
  if(miniwin>=win):
    return "Winner!"
  else:
    return "Loser!"
      #print (ticket[i][0][z])
      #print (ord(ticket[i][0][z]))

