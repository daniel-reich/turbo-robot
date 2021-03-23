"""


A man has `n` number of apples. If he eats a percentage `p` of the apples (if
apples are available), his children will share the remainder of the apples.
Create a function to determine the number of 'whole' apples his children got.
If his children did not get any apples, return `"The children didn't get any
apples"`.

### Examples

    get_number_of_apples(10, "90%") ➞ 1
    
    get_number_of_apples(25, "10%") ➞ 22
    
    get_number_of_apples(0, "10%") ➞ "The children didn't get any apples"

### Notes

`p` will always be given.

"""

def get_number_of_apples(n, p):
    if len(p) == 3:
        res_str = p[:2] + p[3:]
    elif len(p) == 4:
        res_str = p[:3] + p[4:]
    children_get = n - (n * 0.01 * int(res_str))
    if n > 0 and res_str != "100":
        return children_get - (children_get % 1)
    if n <= 0 or res_str == "100":
        return "The children didn't get any apples"

