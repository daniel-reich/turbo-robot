"""


A robot has been given a list of movement instructions. Each instruction is
either `left`, `right`, `up` or `down`, followed by a distance to move. The
robot starts at `[0, 0]`. You want to calculate where the robot will end up
and return its final position as a list.

To illustrate, if the robot is given the following instructions:

    ["right 10", "up 50", "left 30", "down 10"]

It will end up 20 left and 40 up from where it started, so we return `[-20,
40]`.

### Examples

    track_robot(["right 10", "up 50", "left 30", "down 10"]) ➞ [-20, 40]
    
    track_robot([]) ➞ [0, 0]
    // If there are no instructions, the robot doesn't move.
    
    track_robot(["right 100", "right 100", "up 500", "up 10000"]) ➞ [200, 10500]

### Notes

  * The only instructions given will be `left`, `right`, `up` or `down`.
  * The distance after the instruction is always a positive whole number.

"""

def track_robot(instructions):
    instructions = ' '.join(instructions)
    new_instructions = instructions.split()
​
    digit_list = [int(d) for d in new_instructions if d.isdigit()]
    instruction_list = [i for i in new_instructions if not i.isdigit()]
​
    dicto = {'right':0,'up':0,'left':0,'down':0}
    for inst,dig in zip(instruction_list,digit_list):
            if inst in dicto:
                dicto[inst] += dig
            else:
                dicto[inst] == 0
​
    return [dicto.get('right') - dicto.get('left'), dicto.get('up') - dicto.get('down')]

