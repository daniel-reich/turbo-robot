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
    d = list(map(int,duration.split(':')))
    
    t = d[2] + 60*d[1] + 3600*d[0]
    t = t / speed
    
    d[0] = int(t // 3600)
    t = t - d[0] * 3600
    d[1] = int(t // 60)
    t = t- d[1] * 60
    d[2] = int(t)
    
    myans = str(d[0]).zfill(2) + ':' + str(d[1]).zfill(2) + ':' + str(d[2]).zfill(2)
    
    return myans

