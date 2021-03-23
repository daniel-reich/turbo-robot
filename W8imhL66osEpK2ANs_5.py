"""


Given a predetermined rate from a dictionary, write the function that will
return the time it takes for a certain amount of people to paint a certain
amount of walls. Return the minutes as an integer. No rounding is necessary.

### Example

    // It takes 22 minutes for 10 people to paint 10 walls.
    // How many minutes does it take 14 people to paint 14 walls?
    
    let rate = {
      people: 10,
      walls: 10,
      minutes: 22
    }
    
    time(rate, people, walls) ➞ 22

### Notes

Check the **Resources** tab if you get stuck.

"""

def time(dct, people, walls):
  
  start_ppl = dct['people']
  start_walls = dct['walls']
  start_time = dct['minutes']
  
  person_does = (start_walls / start_ppl) / start_time
  print(person_does)
  
  walls_painted = 0
  c = 0
  
  while walls_painted < walls:
    walls_painted += (person_does * people)
    c += 1
  
  return c

