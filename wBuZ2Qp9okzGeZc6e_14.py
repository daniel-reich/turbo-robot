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
  print(road)
  try:
    count = 1
    while road[-count] == "=":
      count += 1
    print(count)
    print(road[-count])
    return road[-count]
  except:
    print(None)
    return None

