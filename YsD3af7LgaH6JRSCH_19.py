"""


In this challenge, you have to add a variable amount of hours, minutes and
seconds to a given time, obtaining, in turn, a new adjusted time.

Given a string `now` being a timestamp in the format `hh:mm:ss`, and three
integers `hrs`, `mins` and `sec` being the hours, minutes and seconds to add,
implement a function that returns a string being the newly adjusted timestamp
(maintaining the same format).

### Examples

    time_adjust("01:00:00", 1, 30, 10) ➞ "02:30:10"
    
    time_adjust("18:22:30", 4, 60, 30) ➞ "23:23:00"
    
    time_adjust("00:00:00", 72, 120, 120) ➞ "02:02:00"

### Notes

  * The amounts of `hrs`, `mins` and `sec` can be any positive integer, and you have to correctly add them to the corresponding unit if they exceed their scale. See example #2: sixty minutes is one hour, and sixty seconds (30 + 30) is one minute.
  * If the amount of time to add exceeds the 24 hours, then the time will start again from "00:00:00". See example #3: 72 hours are 3 exact days so that after three cycles of 24 hours, the hour will be again "00" (and becomes "02" because we are adding also 120 minutes or 2 hours).

"""

def time_adjust(now,hrs, mins, sec):
    sol = ""
    hour = 0
    min = 0
    se = 0
    time = 0
    hour += int(now[0]) * 10
    hour += int(now[1])
    min += int(now[3]) * 10
    min += int(now[4])
    se += int(now[6]) * 10
    se += int(now[7])
    hour += hrs
    min += mins
    se += sec
​
    time += hour * 60 * 60
    time += min * 60
    time += se
    print(hour, min, se)
​
    time /= 60
    time /= 60
​
    ho = time// 1
    print(ho)
    re = time - ho
    re *= 60
    remin = re//1
    print(remin)
    rese = re - remin
    rese *= 60
    print(round(rese, 1))
    if round(rese, 1) == 60:
        remin += 1
        rese = 0
    for x in range(100):
        if ho >= 24 :
            ho -= 24
    print(ho, remin, round(rese, 1))
​
    if ho < 10:
        sol += "0"+str(int(ho))+":"
    else:
        sol += str(int(ho)) + ":"
    if remin < 10:
        sol += "0"+str(int(remin))+":"
    else:
        sol += str(int(remin)) + ":"
    if round(rese, 1) < 10:
        sol += "0"+str(int(round(rese, 1)))
    else:
        sol += str(int(round(rese, 1)))
    print(sol)
    
    return sol

