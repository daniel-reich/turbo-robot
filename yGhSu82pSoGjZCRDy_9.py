"""


A number is **left-heavy** if the digits on the left side are larger than the
digits on the right. It is **right-heavy** if the digits on the right side are
larger than the digits on the left. Else, it is **balanced**.

Create a function that takes in an integer and classifies it into one of the
three mutually exclusive categories: **left** , **right** or **balanced**. For
inputs with an odd number of integers, ignore the fulcrum (the middle number).

### Examples

    seesaw(3449) ➞ "right"
    # since 34 < 49
    
    seesaw(1143113) ➞ "left"
    # since 114 > 113 (3 is the fulcrum)
    
    seesaw(585585) ➞ "balanced"
    # since 585 == 585

### Notes

If input is `None` return `"balanced"`.

"""

def seesaw(num):
    if num is None:
        return "balanced"
    num_arr = [int(d) for d in str(num)]
    if len(num_arr) == 1:
        return "balanced"
    final_arr = []
    if len(num_arr) % 2 == 0:
        final_arr = sum(num_arr[int(len(num_arr) / 2):]), sum(num_arr[:int(len(num_arr) / 2)])
    if len(num_arr) % 2 != 0:
        num_arr.pop(num_arr[round(len(num_arr) / 2) - 1])
        final_arr = sum(num_arr[int(len(num_arr) / 2):]), sum(num_arr[:int(len(num_arr) / 2)])
    if final_arr[0] > final_arr[1]:
        return "right"
    elif final_arr[0] < final_arr[1]:
        return "left"
    else:
        return "balanced"

