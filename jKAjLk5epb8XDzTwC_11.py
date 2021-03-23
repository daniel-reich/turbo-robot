"""


You call your spouse in anger and a "little" argument takes place. Count the
total amount of adjectives used. Given a dictionary of adjectives, return the
total amount of adjectives used.

### Examples

    total_amount_adjectives({ "a": "moron" }) ➞ 1
    
    total_amount_adjectives({ "a": "idiot", "b": "idiot", "c": "idiot" }) ➞ 3
    
    total_amount_adjectives({ "a": "moron", "b": "scumbag", "c": "moron", d: "dirtbag" }) ➞ 4

### Notes

The dictionary will never be empty.

"""

def total_amount_adjectives(obj):
    count = 0
    for adj in obj.values():
        count += 1
    return count
​
​
print(total_amount_adjectives({"a": "moron"}))
print(total_amount_adjectives({"a": "idiot", "b": "idiot", "c": "idiot"}))
print(total_amount_adjectives({"a": "moron", "b": "scumbag", "c": "moron", 'd': "dirtbag"}))

