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

import re, datetime
​
def sync_subs(subtitles, timeIncrement):
  regex = r'\d{2}:\d{2}:\d{2},\d{3}'
  async = re.findall(regex, subtitles)
  incr = ','.join(timeIncrement.split(':')).split(',')
  if not re.match(regex, timeIncrement):
    return 'There is a problem with the second argument'
  else:
    for i in range(3):
      if not 0 <= int(incr[i]) <= 59:
        return 'There is a problem with the second argument'
    if not 0 <= int(incr[3]) <= 999:
      return 'There is a problem with the second argument'
    incrTime = datetime.timedelta(hours=int(incr[0]), minutes=int(incr[1]), seconds=int(incr[2]), microseconds=int(incr[3]))
    b = subtitles
    for time in async:
      a = ','.join(time.split(':')).split(',')
      aTime = datetime.timedelta(hours=int(a[0]), minutes=int(a[1]), seconds=int(a[2]), microseconds=int(a[3]))
      newTime = aTime + incrTime
      s, msec = divmod(newTime.microseconds, 1000)
      minut, sec = divmod(newTime.seconds+s, 60)
      hours, minutes = divmod(minut, 60)
      b = re.sub(time, '{:02}:{:02}:{:02},{:03}'.format(hours,minutes,sec,msec), b)
    return b

