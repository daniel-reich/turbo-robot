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
  if '60' in timeIncrement or not re.match('\d{2}\:\d{2}\:\d{2}\,\d{3}',timeIncrement):
    return 'There is a problem with the second argument'
​
  timeIncrement = [int(i) for i in re.findall('\d+',timeIncrement)]
  if subtitles.count('-->') == 1:
    return align_subtitles(subtitles, timeIncrement)
  else:
    subtitles = subtitles.split('\n')
    subtitles1 = align_subtitles('\n'.join(subtitles[:3]),timeIncrement)
    subtitles2 = align_subtitles('\n'.join(subtitles[3:]),timeIncrement)
    return '\n'.join([subtitles1,subtitles2])
​
def align_subtitles(subtitles, timeIncrement):
  stamp = subtitles[:3]
  arrow = '-->'
  text = subtitles[34:]
​
  time1, time2 = get_times(subtitles)
  time1_up = build_time_string(inc_time(time1,timeIncrement))
  time2_up = build_time_string(inc_time(time2,timeIncrement))
  final_time_string = ' '.join([time1_up, arrow, time2_up])
​
  return '\n'.join([stamp, final_time_string, text])
​
def get_times(txt):
  time1, time2 = re.findall('\d{2}\:\d{2}\:\d{2}\,\d{3}',txt)
  time1 = [int(i) for i in re.findall('\d+',time1)]
  time2 = [int(i) for i in re.findall('\d+',time2)]
  return time1, time2
​
def inc_time(time,inc):
  val = [60,60,1000]
  for i in range(0,-4,-1):
    time[i] += inc[i]
    if time[i] > val[i]:
      time[i] -= val[i]
      time[i-1] += 1
  return time
​
def build_time_string(time):
  h, m, s, ms = time
  return '%02d:%02d:%02d,%03d' % (h, m, s, ms)

