"""


Ted works as a computer programmer at Minecraft Inc. His boss has just given
him an important assignment to update the code for the minecart tracks by the
end of April. However, he has recently had to self-isolate due to Corvid-19
and has left the code for the tracks BACK AT WORK!! He has the shorthand for
the tracks he's supposed to look at, and where the carts are suppost to end
up, but not the actual code.

He knows that:

  1. "-->" = "Speed-Up Track" ⁠— If a minecart interacts with this track, it's velocity increases by 2.67 BPS unless it's at its maximum speed of 8 BPS.
  2. "<\-->" = "Powered Track" ⁠— If a minecart interacts with this track, it's velocity remains the same.
  3. "<\--" = "Slow-Down Track" ⁠— If a minecart interacts with this track, it's velocity decreases by 2.67 BPS unless it's velocity equals 0, at which point it stops.
  4. "---" = "Unpowered Track" ⁠— If a minecart interacts with this track, it's velocity decreases by 1 BPS unless it's velocity equals 0, at which point it stops.

Help Ted by writing a class for the tracks that interact with the provided
Minecart class as shown above. And then write a function that will take a list
of the shorthand tracks and:

  * If the Minecart reaches the last peice of Track, return `True`.
  * Else return the index of the Track where the Minecart stops.

### Examples

    mine_run(["-->", "-->", "-->", "<--", "<--", "<--"]) ➞ True
    
    mine_run(["-->", "<--", "-->", "-->", "<-->", "---"]) ➞ 1

### Notes

N/A

"""

class Minecart:
  def __init__(self, v=0):
    self.v = v
    self.im = self.v > 0
  
  def add_speed(self, speed):
    self.v = min(max(self.v + speed, 0), 8)
    self.im = self.v > 0
​
class Track:
  def __init__(self, _type):
    dic = {'-->': 2.67, '<-->': 0, '<--': -2.67, '---': -1}
    self.mod = dic[_type]
​
  def interact(self, cart):
    cart.add_speed(self.mod)
    
def mine_run(tracks):
  cart = Minecart()
  tracks = [Track(i) for i in tracks]
  for idx, i in enumerate(tracks):
    i.interact(cart)
    if idx+1 == len(tracks): return True
    if not cart.v: return idx

