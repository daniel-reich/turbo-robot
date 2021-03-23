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

class Train:
    def __init__(self, destinations, expected_time):
        self.destinations = destinations
        self.expected_time = expected_time
def manage_delays(train,town,delay):
    print("check1")
    hour = int(train.expected_time.split(":")[0])
    minute = int(train.expected_time.split(":")[1])
    print("check2")
    if town in train.destinations:
        print("check3")
        for i in range(1,delay+1):
            minute += +1
            if minute == 60:
                minute = 0
                hour += 1
                if hour == 24:
                    hour = 0
            else:
                print("check4")
                pass
    print("check5")
    if len(str(hour)) == 1:
        print("check6")
        hour = "0" + str(hour)
    if len(str(minute)) == 1:
        print("check7")
        minute = "0" + str(minute)
    print("check8")
    train.expected_time = str(hour)+":"+ str(minute)

