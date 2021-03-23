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
  import re
  try:
    h, m, s, ms = re.findall("(\d{2}):(\d{2}):(\d{2}),(\d{0,3})",timeIncrement)[0]
    h, m, s, ms = int(h), int(m), int(s), int(ms)
  except:
    m = 61
  if m >= 60 or s >= 60 or ms >= 1000:
    return "There is a problem with the second argument"
    
  for ts in re.findall("(\d{2}):(\d{2}):(\d{2}),(\d{3})",subtitles):
    repstr = "%s:%s:%s,%s" % ts
    nms = int(ts[3])+ms
    carry = 0
    if nms >= 1000:
      nms -= 1000
      carry = 1
    ns = int(ts[2])+s+carry
    if ns >= 60:
      ns -= 60
      carry = 1
    else: 
      carry = 0
    nm = int(ts[1])+m+carry
    if nm >= 60:
      nm -= 60
      carry = 1
    else: 
      carry = 0
    nh = int(ts[0])+h+carry
    subtitles = subtitles.replace(repstr,"%02d:%02d:%02d,%03d" % (nh, nm, ns, nms))
​
  return subtitles

