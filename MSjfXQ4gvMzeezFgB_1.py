"""


The 50-30-20 strategy is a simple way to budget, which involves spending 50%
of after-tax income on needs, 30% after tax income on wants, and 20% after-tax
income on savings or paying off debt.

Given the after-tax income as `ati`, what you are supposed to do is to make a
function that will return a dictionary that shows how much a person needs to
spend on needs, wants, and savings.

### Examples

    fifty_thirty_twenty(10000) ➞ { "Needs": 5000, "Wants": 3000, "Savings": 2000 }
    
    fifty_thirty_twenty(50000) ➞ { "Needs": 25000, "Wants": 15000, "Savings": 10000 }
    
    fifty_thirty_twenty(13450) ➞ { "Needs": 6725, "Wants": 4035, "Savings": 2690 }

### Notes

Check the **Resources** tab if you want to learn more about the 50-30-20
budget strategy.

"""

def fifty_thirty_twenty(ati):
    a = [(ati * 1/2), (ati * 3/10), (ati * 1/5)]
    b = ["Needs", "Wants", "Savings"]
    return dict(zip(b, a))

