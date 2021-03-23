"""


  * `0` represents the dog.
  * Each list represents a house and each `1` represents an empty room.
  * Return the house and the room where it is located, there can be only one dog lost per building.

### Examples

    lost_dog([1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
    ➞ "Dog not found!"
    
    lost_dog([1, 1, 1, 1, 1, 1],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
    ➞ {"Dog1": "House (2) and Room (1)", "Dog2": "House (3) and Room (2)"}
    
    lost_dog([1, 1, 1, 1, 1, 0],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 0, 1, 1, 1])
    ➞ {"Dog1": "House (1) and Room (6)", "Dog2": "House (2) and Room (1)", "Dog3": "House (3) and Room (2)", "Dog4": "House (4) and Room (3)"}

### Notes

Check the **Resources** if you're stuck.

"""

def lost_dog(*args, n=0):
    res = dict()
    for r, row in enumerate(args):
        if 0 in row:
            n += 1
            res["Dog{}".format(n)] = ("House ({}) and Room ({})"
                                      .format(r + 1, row.index(0) + 1))
    return res if n else "Dog not found!"

