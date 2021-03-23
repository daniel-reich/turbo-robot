"""


A country can be said as being big if it is:

  * Big in terms of population.
  * Big in terms of area.

Add to the `Country` class so that it contains the attribute `is_big`. Set it
to `True` if **either** criterea are met:

  * Population is greater than 250 million.
  * Area is larger than 3 million square km.

Also, create a method which compares a country's _population density_ to
another country object. Return a string in the following format:

    {country} has a {smaller / larger} population density than {other_country}

### Examples

    australia = Country("Australia", 23545500, 7692024)
    andorra = Country("Andorra", 76098, 468)
    
    australia.is_big ➞ True
    andorra.is_big ➞ False
    andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"

### Notes

  * Population density is calculated by dividing the population by the area.
  * Area is given in square km.
  * The input will be in the format (name_of_country, population, size_in_km2), where name_of_country is a string and the other two inputs are integers.

"""

class Country:
​
  def __init__(self, name, population, area):
    self.name = name
    self.population = population
    self.area = area
    # implement self.is_big
    self.is_big=False
    if population > 250000000 or area > 3000000:
      self.is_big=True
    
  def compare_pd(self, other):
    # code
    if self.population/self.area > other.population/other.area:
      return(self.name+' has a larger population density than '+other.name)
    elif self.population/self.area < other.population/other.area:
      return(self.name+' has a smaller population density than '+other.name)

