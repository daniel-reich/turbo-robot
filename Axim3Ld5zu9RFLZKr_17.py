"""


Write a function that inverts the keys and values of a dictionary.

### Examples

    invert({ "z": "q", "w": "f" })
    ➞ { "q": "z", "f": "w" }
    
    invert({ "a": 1, "b": 2, "c": 3 })
    ➞ { 1: "a", 2: "b", 3: "c" }
    
    invert({ "zebra": "koala", "horse": "camel" })
    ➞ { "koala": "zebra", "camel": "horse" }

### Notes

N/A

"""

invert=lambda dct:dict(map(reversed, dct.items()))

