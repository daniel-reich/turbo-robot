"""


If a person traveled up a hill for 18mins at 20mph and then traveled back down
the same path at 60mph then their average speed traveled was **30mph**.

Write a function that returns the **average speed** traveled given an uphill
time, uphill rate and a downhill rate. Uphill time is given in **minutes**.
Return the rate as an integer ( **mph** ). No rounding is necessary.

### Examples

    ave_spd(18, 20, 60) ➞ 30
    
    ave_spd(30, 10, 30) ➞ 15
    
    ave_spd(30, 8, 24) ➞ 12

### Notes

  * The solution is **not** dividing the sum of the speeds by 2.
  * Check the **Resources** tab if your stuck.

"""

def ave_spd(up_time, up_spd, down_spd):
    distance = up_spd * (up_time / 60)
    down_time = distance / down_spd
    return 2 * distance / (up_time / 60 + down_time)

