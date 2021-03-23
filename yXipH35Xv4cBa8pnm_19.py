"""


In microwave ovens, when buttons are pressed from 0-9, it will add that number
to the microwave oven timer (starting from the left). All microwave ovens have
the functionality where you can hit a **"+30"** button and it will add **30
seconds** to the timer to cook your food. If you want to heat something for 5
mins, you can hit the "+30" button 10 times instead of thinking if there are
fewer button presses that can give you the same result.

Create a function that takes an argument **time** and returns the shortest
amount of **button presses** to set the given time on the microwave oven. The
microwave oven timer always starts at `00:00`.

### Buttons

    Buttons from "0-9"
    
    # It will add that number to the microwave oven timer (starting from the left).
    # If the number "5" is pressed followed by "0" twice, it will put 05:00 on the timer.
    # If the number "3" is pressed followed by "0", it will put 00:30 on the timer.
    
    Button "+30", which adds 30 seconds to the current timer.
    
    # If the number "+30" is pressed twice, it will put 00:60 on the timer.
    
    A "Start" button which you have to finally press to start the microwave oven.
    
    # Remember to press this!

### Examples

    microwave_buttons("00:30") ➞ 2
    # "+30" to put 30 seconds on the timer.
    # "Start" button to start the oven.
    
    microwave_buttons("00:70") ➞ 3
    # "7" followed by "0" to put 70 seconds on the timer.
    # "Start" button to start the oven.
    
    microwave_buttons("00:00") ➞ 1
    # "Start" button to start the oven.

### Notes

  * Input may not always be what you expect (e.g. you can put in `00:70`, which is valid).
  * No exception handling is required for this challenge.

"""

def microwave_buttons(time):
  a, b = time[::-1] .split(":")
  c = [i+3 for i in range(len(b)) if b[i]!="0"]
  d = [i+1 for i in range(len(a)) if a[i]!="0"]
  e = int(a[::-1])//30 + int(b[::-1])*60 // 30
  if int(a[::-1])<30 and int(b[::-1])==0:
      return sum(c) + sum(d) + 1
  return min(e, sum(c) + sum(d)) + 1

