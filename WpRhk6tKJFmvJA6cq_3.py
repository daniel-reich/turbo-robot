"""


 _Due to unforseen circumstances in Suburbia, the trains will be delayed by a
further 10 minutes._

Create a function that will help to plan out and manage these delays! Create a
function called `manage_delays` that does the following:

  * Parameters will be the train object, a destination and number of minutes the delay is.
  * Increment to the train object's `expected_time` by the delay, **if the destination given is in the train object's destinations**.

### Examples

    trains = [
      Train(["Townsville", "Suburbia", "Urbantska"], "13:04"),
      Train(["Farmsdale", "Suburbia", "Lakeside Valley"], "13:20"),
      Train(["Suburbia", "Townsville", "Lakeside Valley"], "13:22")
    ]
    for t in trains:
        manage_delays(t, "Lakeside Valley", 60)
    
    trains[0].expected_time ➞ "13:04"
    
    trains[1].expected_time ➞ "14:20"
    
    trains[2].expected_time ➞ "14:22"

### Notes

  * Keep in mind that times will be given in **24 hour time**.
  * A train has the attributes `destinations` and `expected_time`. See the **Tests** tab for further details.

"""

"""
class Train:
    def __init__(self, destinations, expected_time):
        self.destinations = destinations
        self.expected_time = expected_time
​
    def get_expected_time(self):
        return self.expected_time
​
    def set_expected_time(self, expected_time):
        self.expected_time = expected_time
​
    def manage_delays(self, dest, delay):
        if dest in self.destinations:
            h, m = [int(_) for _ in self.expected_time.split(':')]
            m += delay
            h += m // 60
            m %= 60
            h %= 24
            new_time = str(h).zfill(2) + ':' + str(m).zfill(2)
            self.expected_time = new_time
        return self.expected_time
"""
​
def manage_delays(train, dest, delay):
    #train.manage_delays(dest, delay)
    #return train.get_expected_time()
    if dest in train.destinations:
        h, m = [int(_) for _ in train.expected_time.split(':')]
        m += delay
        h += m // 60
        m %= 60
        h %= 24
        new_time = str(h).zfill(2) + ':' + str(m).zfill(2)
        train.expected_time = new_time
    return train.expected_time

