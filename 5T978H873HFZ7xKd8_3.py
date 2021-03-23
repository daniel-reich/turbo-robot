"""


Given a class for a `BasicPlan`, write the classes for `StandardPlan` and
`PremiumPlan` which have class attributes of the following:

BasicPlan| StandardPlan| Premium Plan  
---|---|---  
✓| ✓| ✓| can_stream  
✓| ✓| ✓| can_download  
✓| ✓| ✓| has_SD  
| ✓| ✓| has_HD  
| | ✓| has_UHD  
1| 2| 4| num_of_devices  
$8.99| $12.99| $15.99| price  
  
### Examples

    BasicPlan.has_SD ➞ True
    
    PremiumPlan.has_SD ➞ True
    
    BasicPlan.has_UHD ➞ False
    
    BasicPlan.price ➞ "$8.99"
    
    PremiumPlan.num_of_devices ➞ 4

### Notes

Try using _Inheritance_ to complete the challenge! If you're unsure what that
means, try checking out the Python class tutorials in the **Resources** tab.

"""

class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = '$8.99'
​
# Write the classes for StandardPlan and PremiumPlan here!
class StandardPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '$12.99'
    
class PremiumPlan(BasicPlan):
    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = '$15.99'

