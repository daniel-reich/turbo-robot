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
​
    def add_speed(self, speed):
​
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
​
def mine_run(tracks):
    n = 0
    d = {"-->": 2.67, "<-->": 0, "<--": -2.67, "---": 1}
    ja = Minecart(d[tracks[0]])
    for i in tracks[1::]:
        n += 1
        if (len(tracks) - 1) == n:
            return True
        if i in d.keys():
            ja.add_speed(d[i])
            if ja.v <= 0:
                return n
            else:
                pass
    else:
        return True
