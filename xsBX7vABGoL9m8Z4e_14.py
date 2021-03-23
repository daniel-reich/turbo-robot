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
from datetime import datetime
def sync_subs(subtitles, timeIncrement):
  def helper(data):
    tmp=data.group(0)
    tp=datetime.strptime("30 Nov 00 "+tmp,"%d %b %y %H:%M:%S,%f")
    tp=(tp+add)
    return tp.strftime("%H:%M:%S,%f")[:-3]
  try:
    t0=datetime.strptime("30 Nov 00 "+"0:0:0,0","%d %b %y %H:%M:%S,%f")   
    tadd=datetime.strptime("30 Nov 00 "+timeIncrement,"%d %b %y %H:%M:%S,%f")
    add=(tadd-t0)
  except:
    return "There is a problem with the second argument"
​
  print(subtitles)
  new=re.sub('..:..:..,...', helper ,subtitles)
  print(new)
  return new

