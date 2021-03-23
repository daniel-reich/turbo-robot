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
​
  def __init__(self, v=0):
    self.v = v
​
    if self.v <= 0:
      self.im = False
    else:
      self.im = True
  
  def add_speed(self, speed):
    
    if self.im == False:
      self.im = True
​
    if self.v + speed <= 8 and self.v + speed > 0:
      self.v += speed 
    elif self.v + speed <= 0:
      self.v = 0
      self.im = False
    else:
      self.v = 8
​
class Track:
    '''
    Stores the speed for the type of track
    '''
    SPEEDS = {'-->': 2.67, '<-->': 0, '<--': -2.67, '---': -1} # class variable
​
    def __init__(self, track):
        self.velocity = self.SPEEDS[track]
​
def mine_run(tracks):
    '''
    Takes in a list of tracks and returns True if the cart reaches the last one
    otherwise the index of the track where it stops
    '''
    cart = Minecart()
​
    for i, track in enumerate(tracks):
        cart.add_speed(Track(track).velocity)
        if cart.v == 0:
            return True if i == len(tracks) - 1 else i

