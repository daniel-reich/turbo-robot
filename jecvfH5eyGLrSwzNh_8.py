"""


Create a function that takes a string containing both name and number of
animals and plants that may or may not be found in Chitwan National Park. The
function should return a list of tuples where first element in the tuple is
animal name and second element in the tuple is number of that particular
animal that is found in Chitwan National Park.

### Animals Present in Chitwan National Park

    animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]

### Examples

    fauna_number("There are 24 one-hornedrhino,50 python and 20000 mango.") ➞ [("one-hornedrhino", "24"), ("python", "50")]
    # Mango not present in animal list.
    
    fauna_number("There are 244 bengaltiger,200 monitorlizard and 5000 apples .") ➞ [("bengaltiger", "244"), ("monitorlizard", "200")]
    # Apples not present in animal list.

### Notes

  * Input contains name and number of both animals and plants.
  * If there is no match, return an empty list.

"""

def fauna_number(s):
    '''
    Returns a list of tuples (animal, n) where animal is present in Chitwan
    National Park and n is the number of this animal in s.
    '''
    animals = ["muggercrocodile", "one-hornedrhino", "python", "moth",
               "monitorlizard", "bengaltiger"]
    s = s.replace(',',' ').replace('.',' ').split()
    
    return [(animal, s[i-1]) for i, animal in enumerate(s)
            if animal in animals]

