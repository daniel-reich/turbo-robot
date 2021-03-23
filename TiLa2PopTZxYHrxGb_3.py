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
    '''
    Returns the duration adjusted for speed as per instructions
    '''
    h,m,s = (int(t) for t in duration.split(':'))
    d2 = int((h*3600 + m*60 + s)/speed)
    h2 = d2 // 3600
    m2 = (d2 - h2*3600) // 60
    s2 = d2 - h2*3600 - m2*60
​
    return '{:02d}:{:02d}:{:02d}'.format(h2,m2,s2)

