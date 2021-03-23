"""


Suppose you are directionally challenged, and get lost easily. As a result,
sometimes you walk in circles or make U-turns. You might take a sub-optimal
route. Create a function that returns the difference in length between **your
path** and the **optimal path**. Both paths reach the same destination.

You start at `(0,0)` and reach your destination by the end of the input list.

A demonstration:

    Your route: ["N", "S", "E", "W", "E", "E", "E", "N"]  // 8
    Optimal route: ["E", "E", "E", "N"] (or ["N", "E", "E", "E"], etc.) // 4
    # Difference in length: 8 - 4 = 4
    
    # Explanation: Your "S" cancels out your "N" and your "W" cancels out your "E" leaving you back at (0,0)

### Examples

    route_diff(["N", "E", "S", "W"]) ➞ 4
    # You"ve just walked in a circle! You are back at the origin. Your optimal path was `[]`.
    
    route_diff(["N", "N", "N", "E", "N", "E"]) ➞ 0
    # No improvements here!
    
    route_diff(["N", "S", "N", "S", "E", "W", "E", "E"]) ➞ 6

### Notes

Remember that a `N` cancels out a `S`, and an `E` cancels out a `W`.

"""

def route_diff(directions):
    pass
    pos = get_position(directions)
    
    return len(directions) - abs(pos[0]) - abs(pos[1])
​
def get_position(directions):
​
    ns_dir = 0
    ew_dir = 0
​
    for dir in directions:
​
        if dir == "N":
            ns_dir += 1
        elif dir == "S":
            ns_dir -= 1
        elif dir == "E":
            ew_dir += 1
        else:
            ew_dir -= 1
​
    return (ew_dir, ns_dir)
​
​
directions = ["N", "S", "N", "S", "E", "W", "E", "E"]
​
print(route_diff(directions))

