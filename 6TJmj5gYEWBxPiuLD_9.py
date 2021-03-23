"""


Create a function that reads a list of integers stored which will be in the
following format: `[[K, r1, r2, r3, ...]]`, where **K** represents the number
of desks in a classroom, and the rest of the integers in the list will be in
sorted order and will represent the desks that are already occupied. All of
the desks will be arranged in two columns, where desk #1 is at the top left,
desk #2 at the top right, desk #3 is below #1, desk #4 is below #2, etc.

Your program should return the number of ways two students can be seated next
to each other. This means one student is on the left and one on the right, or
one student is directly above or below the other student.

To illustrate:

    [[12, 2, 6, 7, 11]]

This classroom will look like the following:

#### Column 1

    [[#, 4, #, 8, 10, 12]]
    # The first # is 2 and second # is 6 which are occupied.

#### Column 2

    [[1, 3, 5, #, 9, #]]
    # The first # is 7 and and second # is 11 which are occupied.

Based on the above arrangement of occupied desks, there are a total of six
ways to seat two new students next to each other. The combinations are:

    [[1, 3]], [[3, 4]], [[3, 5]], [[8, 10]], [[9, 10]], [[10, 12]]

For this input, your program should return `6`. **K** will range from `2` to
`24` and will always be an even number. After **K** , the number of occupied
desks in the list can range from `0` to **K**.

### Examples

    seating_students([6, 4]) ➞ 4
    
    seating_students([8, 1, 8]) ➞ 6
    
    seating_students([12, 2, 6, 7, 11])  ➞ 6

### Notes

N/A

"""

def seating_students(lst):
​
  class Classroom:
    class Seat:
​
      def __init__(self, ident, maxid, occupied = False):
        self.id = ident
        self.occ = occupied
        self.mid = maxid
​
        self.nearby = []
​
        if self.id not in [1, 2]:
          self.nearby.append(self.id - 2)
        if self.id % 2 == 0:
          self.nearby.append(self.id - 1)
        else:
          self.nearby.append(self.id + 1)
        if self.id not in [self.mid - 1, self.mid]:
          self.nearby.append(self.id + 2)
    
    def __init__(self, num_of_seats):
      self.nos = num_of_seats
      self.seats = {}
​
      for n in range(1, self.nos + 1):
        self.seats[n] = Classroom.Seat(n,self.nos)
    
    def occupy(self, seat):
      self.seats[seat].occ = True
      return True
    
    def count_unocc_pairs(self):
      unocc_pairs = set()
      for sid in self.seats.keys():
        seat = self.seats[sid]
        if seat.occ == True:
          continue
        nearby_seats = seat.nearby
        for nsid in nearby_seats:
          if self.seats[nsid].occ == False:
            pair = ','.join(sorted([str(sid), str(nsid)]))
            unocc_pairs.add(pair)
      return len(list(unocc_pairs))
​
  classroom = Classroom(lst[0])
​
  for chair in lst[1:]:
    classroom.occupy(chair)
  
  return classroom.count_unocc_pairs()

