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
def sync_subs(subtitles, timeIncrement):
  #handle incorrect timeIncrement
  y=timeIncrement.split(':')
  if (len(y)==3):
    if len(y[0])!=2 or len(y[1])!=2 or len(y[2])!=6 or int (y[0])>=60\
    or int (y[1])>=60 or ',' not in y[2]:
      return('There is a problem with the second argument')
  else:
    return('There is a problem with the second argument')
​
  subtitles1=subtitles
  strings,overflow=re.findall('[\w\W\s\S\d\D](\d{2}:\d{2}:\d{2},\d{3})[\w\W\s\S\d\D]',subtitles),0
  for i in range(len(strings)):
    first = strings[i]
    fraction,overflow = (int(first.split(',')[-1])+ int(timeIncrement.split(',')[-1])),0
    if(fraction >=1000):
      fraction,overflow  = fraction-1000,1
    fraction=str(fraction)
    while not  (len(fraction)==3):
      fraction = '0'+fraction
    
    seconds = overflow+ int(first.split(',')[0].split(':')[-1]) + int(timeIncrement.split(',')[0].split(':')[-1])
    if seconds >=60:
      seconds, overflow = seconds-60,1
    else:
      overflow=0
    seconds=str(seconds)
    if len(seconds)==1:
      seconds = '0'+seconds
    
    minutes = overflow+ int(first.split(',')[0].split(':')[1]) + int(timeIncrement.split(',')[0].split(':')[1])
    if minutes >=60:
      minutes, overflow = minutes-60,1
    else:
      overflow=0
    minutes=str(minutes)
    if len(minutes)==1:
      minutes = '0'+minutes
    
    hours = overflow+ int(first.split(',')[0].split(':')[0]) + int(timeIncrement.split(',')[0].split(':')[0])
    if hours >=23:
      hours=hours%24
    hours=str(hours)
    if len(hours)==1:
      hours = '0'+hours
    subtitles1=subtitles1.replace(first,hours+':'+minutes+':'+seconds+','+fraction)
  return subtitles1

