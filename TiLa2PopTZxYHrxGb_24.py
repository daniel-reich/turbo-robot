"""


YouTube offers different playback speed options for users. This allows users
to increase or decrease the speed of the video content. Given the actual
`duration` and playback `speed` of the video, calculate the **playback
duration** of the video.

### Examples

    playback_duration("00:30:00", 2) ➞ "00:15:00"
    
    playback_duration("01:20:00", 1.5) ➞ "00:53:20"
    
    playback_duration("51:20:09", 0.5) ➞ "102:40:18"

### Notes

  * Both durations will be in hh:mm:ss format.
  * Playback speed will be up to one decimal place only.
  * Time units are expected to be **truncated/floored**.

"""

def playback_duration(duration, speed):
    h,m,s=duration.split(':')
    totSec=(3600*int(h)+60*int(m)+int(s))/speed
    h=totSec//3600
    totSec=totSec%3600
    m=totSec//60
    s=totSec%60
    return str('{:02d}:{:02d}:{:02d}'.format(int(h),int(m),int(s)))

