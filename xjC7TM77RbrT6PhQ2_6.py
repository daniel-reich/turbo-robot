"""


Deep inside a secure mountain facility there exists a group of switches
arranged in a horizontal row. The rightmost switch can be flipped on or off at
any time. Any other switch can be toggled only if the switch to its immediate
right is turned **on** and all other switches to the right are turned **off**.

All the switches are initially **off**. Improvise a function that accepts the
number of switches, `n`, and returns the **minimum number** of switch toggles
required to turn all the switches **on**.

### Examples

    switches(1) ➞ 1
    
    switches(2) ➞ 2
    
    switches(3) ➞ 5
    # Minimal sequence for 3 switches:
    # 000, 001, 011, 010, 110, 111
    
    switches(4) ➞ 10

### Notes

N/A

"""

def switches(n):
    if n == 1:
        return 1
    toggles = {tuple([0] * n): 0}
    target = [1] * n
    queue = [[0] * n]
    while len(queue) > 0:
        cur = queue.pop(0)
        # toggle right-most switch:
        new1 = cur[:]
        new1[n - 1] = 1 - new1[n - 1]
        if tuple(new1) not in toggles:
            queue.append(new1[:])
            toggles[tuple(new1)] = toggles[tuple(cur)] + 1
            if new1 == target:
                return toggles[tuple(new1)]
        # toggle additional switch if possible:
        for i in range(n - 1, 0, -1):
            if cur[i] == 1:
                new2 = cur[:]
                new2[i - 1] = 1 - new2[i - 1]
                if tuple(new2) not in toggles:
                    queue.append(new2[:])
                    toggles[tuple(new2)] = toggles[tuple(cur)] + 1
                    if new2 == target:
                        return toggles[tuple(new2)]
                break

