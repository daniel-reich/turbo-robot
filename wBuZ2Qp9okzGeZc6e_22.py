"""


Create a function that takes a string `road` and returns the car that's in
first place. The road will be made of "=", and cars will be represented by
letters in the alphabet.

### Examples

    first_place("====b===O===e===U=A==") ➞ "A"
    
    first_place("e==B=Fe") ➞ "e"
    
    first_place("proeNeoOJGnfl") ➞ "l"

### Notes

Return `None` if there are no cars on the road or if there is no road.

"""

def first_place(road):
  if any(i.isalpha() for i in road) == True:
    return [i for i in road if i != "="][-1]
  else:
    return None

