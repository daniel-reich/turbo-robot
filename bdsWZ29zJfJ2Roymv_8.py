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
    extra = []
    arr = []
    if len(txt) >= 4:
        for i in range(len(txt))[::4]:
            arr.append(txt[i:i + 4])
        if len(arr[-1]) != 4:
            extra.append(arr[-1])
            arr = arr[:-1]
​
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i][2:] + arr[i][:2])
​
    if len(txt) < 4:
        return txt
    elif len(txt) % 4 and len(txt) > 4:
        return "".join(answer) + extra[0]
    return "".join(answer)

