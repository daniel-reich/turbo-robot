"""


Given an RGB(A) CSS color, determine whether its format is valid or not.
Create a function that takes a string (e.g. `"rgb(0, 0, 0)"`) and return
`True` if it's format is correct, otherwise return `False`.

### Examples

    valid_color("rgb(0,0,0)") ➞ True
    
    valid_color("rgb(0,,0)") ➞ False
    
    valid_color("rgb(255,256,255)") ➞ False
    
    valid_color("rgba(0,0,0,0.123456789)") ➞ True

### Notes

  * Alpha is between 0 and 1.
  * There are a few edge cases (check out the **Tests** tab to know more).

"""

def valid_color(color):
    if color.startswith("rgb(") or color.startswith("rgba("):
        num_txt = color.strip("rgba()")
        num_lst = num_txt.split(",")
        check = 0
        for i in num_lst:
            if bool(i) == True:
                check += 1
        if (color.startswith("rgb(") == True and check != 3) or (color.startswith("rgba(") == True and check != 4): return False
        check_lst = list()
        for i in num_lst:
            if "%" in i:
                if 0 <= int(i.strip(" %")) <= 100: check_lst.append(True)
                else: check_lst.append(False)
            elif "." not in i:
                if 0 <= int(i.strip(" ")) <= 255:check_lst.append(True)
                else: check_lst.append(False)
            elif "." in i:
                if float(i.strip(" ")) < 1:check_lst.append(True)
                else:check_lst.append(False)
        return all(check_lst)
    else: return False

