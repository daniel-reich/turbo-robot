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

def sync_subs(subtitles, timeIncrement):
  if problem(timeIncrement): return 'There is a problem with the second argument'
  subtitles = subtitles.split('\n')
  for i in range(len(subtitles)):
    if '-->' in subtitles[i]:
      subtitles[i] = fixtime(timeIncrement,subtitles[i])
  return '\n'.join(subtitles)
​
def fixtime(inc, time):
  inc = inc.split(':')
  inc = inc[:-1]+inc[-1].split(',')
  time = time.split(' --> ')
  for i in range(len(time)):
    temp = time[i].split(':')
    temp = temp[:-1]+temp[-1].split(',')
    for x in range(len(temp)):
      temp[x] = int(temp[x])+int(inc[x])
    if temp[3] >= 1000:
      temp[2] += temp[3]//1000
      temp[3] = temp[3]%1000
    if temp[2] >=60:
      temp[1] += temp[2]//60
      temp[2] = temp[2]%60
    if temp[1] >= 60:
      temp[0] += temp[1]//60
      temp[1] = temp[1]%60
    temp = [str(i) for i in temp]
    for x in range(3):
      if len(temp[x]) < 2:
        if len(temp[x]) ==1: temp[x] = '0'+temp[x]
    if len(temp[3])<3:
      if len(temp[3])==1: temp[3] = '00'+temp[3]
      else: temp[3] = '0' + temp[3]
    temp = temp[0]+':'+temp[1]+':'+temp[2]+','+temp[3]
    time[i] = temp
  return ' --> '.join(time)
  
def problem(inc):
  if inc.count(':') != 2 or inc.count(',') != 1: return True
  inc = inc.split(':')
  inc = inc[:-1] + inc[-1].split(',')
  for i in range(3):
    if int(inc[i])>=60: return True
  if int(inc[-1])>=1000: return True
  return False

