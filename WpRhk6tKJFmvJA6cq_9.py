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
  if dest in train.destinations:
​
    time = train.expected_time
​
    x = time.split(":")
    y = [int(i) for i in x]
    print(y)
​
    if delay == 60: 
      y[0] = y[0] + 1 
    elif delay > 60: 
      y[0] = y[0] + delay // 60
      if delay % 60 == 0: 
        pass 
      else:
        if (y[1] + delay % 60) // 60 == 1:
          y[0] = y[0] + 1
          y[1] = (y[1] + delay % 60) % 60  
        else:
          y[1] = y[1] + delay % 60 
    elif delay < 60:
      y[1] = y[1] + delay 
​
    z = ""
    z += str(y[0])
    z += ":"
    if len(str(y[1])) == 2:
      pass
    else:  
      z += str(0)
    z += str(y[1])
    train.expected_time = z

