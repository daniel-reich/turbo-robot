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
    s=[1,2,0]
    if n<3:
        return s[n-1]
    for i in range(2,n):
        s[i]=s[i-1]+2*s[i-2]+1
        s.append(s[i])
    return s[n]

