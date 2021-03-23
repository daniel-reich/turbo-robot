"""


Write a function to return the city from each of these vacation spots.

### Examples

    grab_city("[Last Day!] Beer Festival [Munich]") ➞ "Munich"
    
    grab_city("Cheese Factory Tour [Portland]") ➞ "Portland"
    
    grab_city("[50% Off!][Group Tours Included] 5-Day Trip to Onsen [Kyoto]") ➞ "Kyoto"

### Notes

There may be additional brackets, but the city will always be in the last
bracket pair.

"""

def grab_city(txt):
  return txt.split("[")[-1][:-1]

