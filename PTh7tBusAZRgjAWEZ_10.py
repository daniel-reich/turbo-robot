"""


The insurance guy calls again and apologizes. They found another policy made
by your spouse, but this one is limited to cover a particular maximum in
losses (for example, 50,000€). You send a bill to your spouse for the
difference you lost.

Given an _dict_ of the stolen items and a _limit_ , return the difference
between the total value of those items and the limit of the policy.

### Examples

    calc_diff({ "baseball bat": 20 }, 5) ➞ 15
    
    calc_diff({"skate": 10, "painting": 20 }, 19) ➞ 11
    
    calc_diff({"skate": 200, "painting": 200, "shoes": 1 }, 400) ➞ 1

### Notes

  * The _dict_ data always contains at least an item ( _no empty objects_ ).
  * The sum of the items is always greater than the limit.

"""

def calc_diff(obj, limit):
    return sum(obj.values()) - limit
print(calc_diff({'baseball bat': 20},5))
print(calc_diff({'skate': 10, 'painting': 20},19))
print(calc_diff({'skate': 200, 'painting': 200, 'shoes': 1},400))

