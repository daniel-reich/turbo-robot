"""


Create a function that takes a country's `name` and its `area` as arguments
and returns the area of the country's proportion of the total world's
landmass.

### Examples

    area_of_country("Russia", 17098242) ➞ "Russia is 11.48% of the total world's landmass"
    
    area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass"
    
    area_of_country("Iran", 1648195) ➞ "Iran is 1.11% of the total world's landmass"

### Notes

  * The total world's landmass is `148,940,000` [Km^2]
  * Round the result to two decimal places.
  * If you get stuck on a challenge, find help in the **Resources** tab.

"""

def area_of_country(name, area):
  return "{name} is {perc}% of the total world's landmass".format(name = name, perc = round((area/148940000) * 100, 2))

