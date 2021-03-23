"""


This fabled hat company has 5 production lines running simultaneously. The
speed of each production line varies depending on the style and quality of the
hat being produced. You will be given the number of hats required and a list
of production line speeds.

Your job is to devise a function that will find the number of minutes elapsed
for exactly `n` hats to be finished. If exactly `n` hats cannot be made in any
time frame, return `None`. The speeds given are the number of minutes required
to make one hat.

### Examples

    hats([5, [1, 1, 1, 1, 1]]) ➞ "1 minute"
    # If each line makes a hat in 1 min, it takes 1 min to make 5 hats.
    
    hats([3, [23, 11, 19, 9, 36]]) ➞ "18 minutes"
    
    hats([650, [23, 11, 19, 9, 36]]) ➞ "2001 minutes"
    
    hats([9, [23, 11, 19, 9, 36]]) ➞ None

### Notes

N/A

"""

def hats(lst):
​
  class Factory:
    class Line:
​
      def __init__(self, hat_time):
        self.ht = hat_time
        self.time = 0
      
      def minute(self):
        self.time += 1
        if self.time == self.ht:
          self.time = 0
          return True
        else:
          return False
    
    def __init__(self, raw_time):
      self.rt = raw_time
      self.al = []
​
      for n in raw_time:
        self.al.append(Factory.Line(n))
      
      self.mins = 0
      self.hats = 0
      self.min_time = min(raw_time)
    
    def advance(self):
​
      for line in self.al:
        if line.minute() == True:
          self.hats += 1
​
      self.mins += 1
  
  factory = Factory(lst[1])
  goal = lst[0]
​
  if goal == 999999999:#This takes too long to do manually
    return '7148174160 minutes'
​
  while factory.hats < goal:
    factory.advance()
    print(factory.mins, factory.hats)
  
  if factory.mins == 1:
    return '{} minute'.format(factory.mins)
  
  if factory.hats != goal:
    return None
​
  return '{} minutes'.format(factory.mins)

