"""


Create the function that takes a list of dictionaries and returns the sum of
people's budgets.

### Examples

    get_budgets([
      { "name": "John", "age": 21, "budget": 23000 },
      { "name": "Steve",  "age": 32, "budget": 40000 },
      { "name": "Martin",  "age": 16, "budget": 2700 }
    ]) ➞ 65700
    
    get_budgets([
      { "name": "John",  "age": 21, "budget": 29000 },
      { "name": "Steve",  "age": 32, "budget": 32000 },
      { "name": "Martin",  "age": 16, "budget": 1600 }
    ]) ➞ 62600

### Notes

N/A

"""

def get_budgets(mylist2):
    total = 0
    for dictionary in mylist2:
        total += dictionary['budget']
    return total

