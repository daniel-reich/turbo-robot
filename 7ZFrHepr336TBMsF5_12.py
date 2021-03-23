"""


Create a function that takes an old price `old`, a new price `new`, and
returns what percent the price decreased or increased. Round the percentage to
the nearest whole percent.

### Examples

    percentage_changed("$800", "$600") ➞ "25% decrease"
    
    percentage_changed("$1000", "$840") ➞ "16% decrease"
    
    percentage_changed("$100", "$950") ➞ "850% increase"

### Notes

N/A

"""

def percentage_changed(old, new):
    num_new = int(new[1:])
    num_old = int(old[1:])
    changed = int(num_new - num_old)
    changed_percentage = abs(round((changed / num_old) * 100))
​
    if num_old > num_new:
        return "{}% decrease".format(changed_percentage) 
    elif num_old < num_new:
        return "{}% increase".format(changed_percentage)

