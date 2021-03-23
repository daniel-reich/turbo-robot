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

def percentage_changed(old,new):
    
    old = int(old[1:])
    new = int(new[1:])
​
    result = int(((new-old)/old)*100)
​
    if result < 0:
        result = -1 * result
        return "{}% decrease".format(result)
    else:
        return "{}% increase".format(result)

