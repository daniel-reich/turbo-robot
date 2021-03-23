"""


This classic problem dates back to Roman times. There are 41 soldiers arranged
in a circle. Every third soldier is to be killed by their captors, continuing
around the circle until only one soldier remains. He is to be freed. Assuming
you would like to stay alive, at what position in the circle would you stand?

Generalize this problem by creating a function that accepts the number of
soldiers `n` and the interval at which they are killed `i`, and returns the
position of the fortunate survivor.

### Examples

    josephus(41, 3) ➞ 31
    
    josephus(35, 11) ➞ 18
    
    josephus(11, 1) ➞ 11
    
    josephus(2, 2) ➞ 1

### Notes

  * Assume the positions are numbered 1 to `n` going **clockwise** around the circle.
  * If the interval is 3, the first soldiers to die are at positions 3, 6, and 9.

"""

from collections import defaultdict
def josephus(people, step):
    soldiers = list(range(people))
    is_alive = {i: True for i in range(people)}
    pos = 0
    while len([k for k,v in is_alive.items() if v]) > 1:
        cnt_alive = 0
        if is_alive[pos]:
            cnt_alive += 1
        while cnt_alive < step:
            pos = (pos + 1) % len(soldiers) 
            if is_alive[pos]:
                cnt_alive += 1     
        is_alive[pos] = False
    return [k for k,v in is_alive.items() if v][0] +1

