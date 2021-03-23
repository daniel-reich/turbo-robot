"""


A long stretch of beach is represented by a string of two characters `0` \-
free, `1` \- occupied. Due to recent restrictions, a new person cannot take
place next to another. There has to be one free place between two people
lounging on the beach. Create a function to compute how many new people at
most can settle in on the given beach.

### Examples

    sun_loungers("10001") ➞ 1
    # Can take place in the middle.
    
    sun_loungers("00101") ➞ 1
    # Can take place on the left.
    
    sun_loungers("0") ➞ 1
    # Can take one place.
    
    sun_loungers("000") ➞ 2
    # Can take places on the left and on the right.

### Notes

N/A

"""

def sun_loungers(beach):
  
  class Beach:
    class Space:
      
      def __init__(self, place, maxplace, lounger = False):
        self.p = place
        self.near = []
        if self.p != 0:
          self.near.append(place-1)
        if self.p != maxplace:
          self.near.append(place+1)
        self.lounger = lounger
      
      def is_possible(self, places):
        if self.lounger == True:
          return False
        for place in self.near:
          if places[place].lounger == True:
            return False
        return True
      
      def make_lounger(self):
        self.lounger = True
        return True
    
    def __init__(self, beach):
      
      self.beach = beach
      self.spaces = {}
      self.olc = 0
      
      for n in range(len(beach)):
        self.spaces[n] = Beach.Space(n, len(beach) - 1, beach[n] == '1')
        if beach[n] == '1':
          self.olc += 1
    
    def max_out_loungers(self):
      
      for n in range(len(self.beach)):
        place = self.spaces[n]
        if place.is_possible(self.spaces) == True:
          place.make_lounger()
      return True
    
    def count_loungers(self):
      count = 0
      for place in self.spaces.values():
        if place.lounger == True:
          count += 1
      return count
  
  beach = Beach(beach)
  #print(beach.olc)
  beach.max_out_loungers()
  #print(beach.count_loungers(), beach.olc)
  return beach.count_loungers() - beach.olc

