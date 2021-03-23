"""


Create a function that will increment every time format found in a string (for
example `00:42:33,120`) by a specific time (for example `00:00:30,550`). The
result between the examples is `00:43:03,670`.

### Rules

  * The function must take 2 arguments: a string from where to search time format and a string that respects the format `hours:minutes:seconds,milliseconds`.
  * The function must return a string identical to the first argument but with all time format incremented with the second argument time format.
  * If the second argument does not respect the given time format (for example `00:00:00` or `0:0:0,000`), you must return "There is a problem with the second argument".

### Examples

    sync_subs("708
    00:44:50,006 --> 00:44:53,007
    Hi.", "00:03:30,550")
    ➞
    "708
    00:45:20,556 --> 00:45:23,557
    Hi."
    
    sync_subs("179
    00:12:52,766 --> 00:12:55,900
    [Door rattling]", "00:11:11,111")
    ➞
    "179
    00:24:04,011 --> 00:24:07,011
    [Door rattling]"
    
    sync_subs("188
    00:13:37,243 --> 00:13:39,744
    30 minutes.
    Everyone's ready.
    189
    00:13:39,779 --> 00:13:43,548
    
    ", "01:00:51,111")
    ➞
    "188
    02:06:28,000 --> 02:06:30,000
    30 minutes.
    Everyone's ready.
    189
    02:06:30,000 --> 02:06:34,000"

### Notes

You don't need to worry about a time format being wrong in the first string
like `00:13:79,779` or `00:13:39,79` because there won't be any mistake in it.

"""

import re
import datetime
import time
​
def sync_subs(subtitles, timeIncrement):
​
  match=re.compile(r"\d\d:\d\d:\d\d,\d\d\d")
​
  try:
      time.strptime(timeIncrement.replace(",",":")+"000","%H:%M:%S:%f")
  except ValueError:
      return "There is a problem with the second argument"
​
  add_hours=int(timeIncrement[:2])
  add_minutes=int(timeIncrement[3:5])
  add_seconds=int(timeIncrement[6:8])
  add_milliseconds=int(timeIncrement[9:])
  date_new=datetime.timedelta(hours=add_hours,minutes=add_minutes,seconds=add_seconds,milliseconds=add_milliseconds)
​
  for num, i in enumerate(re.finditer(match,subtitles)):
      start=i.start()
      hours=int(subtitles[start:start+2])
      minutes=int(subtitles[start+3:start+5])
      seconds=int(subtitles[start+6:start+8])
      milliseconds=int(subtitles[start+9:start+12])
      date_old=datetime.timedelta(hours=hours,minutes=minutes,seconds=seconds,milliseconds=milliseconds)
      final_time="0"+str(date_old+date_new)[:-3].replace(".",",")
      subtitles=subtitles.replace(subtitles[start:start+12],final_time)
    
  return subtitles

