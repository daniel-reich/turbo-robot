"""


A game of table tennis almost always sounds like _Ping!_ followed by _Pong!_
Therefore, you know that Player 2 has won if you hear _Pong!_ as the last
sound (since Player 1 didn't return the ball back).

Given a list of _Ping!_ , create a function that inserts _Pong!_ in between
each element. Also:

  * If `win` equals `True`, end the list with _Pong!_.
  * If `win` equals `False`, end with _Ping!_ instead.

### Examples

    ping_pong(["Ping!"], True) ➞ ["Ping!", "Pong!"]
    
    ping_pong(["Ping!", "Ping!"], False) ➞ ["Ping!", "Pong!", "Ping!"]
    
    ping_pong(["Ping!", "Ping!", "Ping!"], True) ➞ ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"]

### Notes

  * You will always return the ball (i.e. the Pongs are yours).
  * Player 1 serves the ball and makes _Ping!_.
    * Return a list of strings.

"""

def ping_pong(lst, win):
  out = []
  if win == True:
    for i in lst:
      out.append(i)
      out.append('Pong!')
    return out
  else:
    for i in range(0,len(lst)):
      out.append(lst[i])
      if i != len(lst)-1:
        out.append('Pong!')
    return out

