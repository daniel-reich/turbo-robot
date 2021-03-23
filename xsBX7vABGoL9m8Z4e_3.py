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

from datetime import timedelta
import re
​
def sync_subs(subtitles, timeIncrement):
    timeRegEx = re.compile(r'\b(0\d|1\d|2[0-3]):([0-5]\d):([0-5]\d),(\d{3})\b')
    mo_incr = timeRegEx.match(timeIncrement)
    if mo_incr == None:
        return "There is a problem with the second argument"
    else:
        match_incr = timeRegEx.findall(timeIncrement)
        h,m,s,ms = match_incr[0]
        t_incr = timedelta(
            hours=int(h),
            minutes=int(m),
            seconds=int(s),
            milliseconds=int(ms)
            )
        L = subtitles.split('\n')
        new = []
        for line in L:    
            mo_sub = timeRegEx.search(line)
            if  not mo_sub:
                new.append(line)
            else:
                match_line = line.split(' --> ')
                new_line = []
                for element in match_line:
                    match = timeRegEx.findall(element)
                    a,b,c,d = match[0]
                    t_old = timedelta(
                        hours=int(a),
                        minutes=int(b),
                        seconds=int(c),
                        milliseconds=int(d)
                        )
                    t_new = t_old + t_incr
                    H = t_new.seconds//3600
                    M = t_new.seconds%3600//60
                    S = t_new.seconds - H*3600 - M*60
                    MS = t_new.microseconds//1000
                    new_line.append('{:02}:{:02}:{:02},{}'.format(H, M, S, MS))
                    new_str = ' --> '.join(new_line)
                new.append(new_str)
    return '\n'.join(new)

