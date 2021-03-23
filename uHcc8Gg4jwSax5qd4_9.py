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
    def __init__(self, ln):
        self.v = 0
        self.index = 0
        self.result = 0
        self.len = ln
​
    def add_speed(self, speed):
        print(speed)
        if (self.result == 0 ):  
            if(self.v > 0 or self.index == 0):
                self.index += 1
                if ( self.v <= 8):
                    if (self.v + speed >= 8):
                        self.v = 8
                    elif (self.v + speed <= 0 and self.index != self.len):
                        self.v = 0
                        self.result = self.index
                    elif(self.index == self.len):
                        self.result = 0
                    else:
                        self.v += speed 
            else:
                self.result = self.index
​
    def checkResult(self):
        if (self.result == 0):
            return True
        else:
            return self.result - 1
​
def mine_run(tracks):
    rules = {"-->": +2.67, "<-->": 0, "<--": -2.67, "---": -1}
    new_Mine = Minecart(len(tracks))
    for n in tracks:
        new_Mine.add_speed(rules[n])
    return new_Mine.checkResult()

