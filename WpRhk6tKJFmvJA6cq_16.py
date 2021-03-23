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

def manage_delays(train, dest, delay):
  hr_min = train.expected_time.split(':')
  for d in train.destinations:
    if d == dest:
      hr_min[1] = int(hr_min[1]) + delay
  if int(hr_min[1]) > 59:
    hr_min[0] = int(hr_min[0]) + int(hr_min[1]/60)
    hr_min[1] = hr_min[1] % 60
  if len(str(hr_min[1])) < 1.5:
    train.expected_time = str(hr_min[0]) + ':0' + str(hr_min[1])
  else:
    train.expected_time = str(hr_min[0]) + ':' + str(hr_min[1])

