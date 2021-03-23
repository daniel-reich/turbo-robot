"""


Write a function that swaps the first **pair** (1st and 2nd characters) with
the second **pair** (3rd and 4th characters) for every quadruplet substring.

### Examples

    swap_two("ABCDEFGH") ➞ "CDABGHEF"
    
    swap_two("AABBCCDDEEFF") ➞ "BBAADDCCFFEE"
    
    swap_two("munchkins") ➞ "ncmuinhks"
    
    swap_two("FFGGHHI") ➞ "GGFFHHI"

### Notes

Keep **leftover strings** in the same order.

"""

def swap_two(txt):
    if not len(txt) % 4:
        nl = [txt[i:i+4] for i in range(0, len(txt), 4)]
        return ''.join(w[2]+w[3]+w[0]+w[1] for w in nl)
    else:
        nl = [txt[i:i+4] for i in range(0, len(txt)//4*4, 4)]
        return ''.join(w[2]+w[3]+w[0]+w[1] for w in nl)+txt[len(txt)//4*4:]

