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
    duration_split = duration.split(':')
    hours = int(duration_split[0])
    minutes = int(duration_split[1])
    seconds = int(duration_split[2])
    total_seconds = 0
    while hours > 0:
        total_seconds += 3600
        hours -= 1
    while minutes > 0:
        total_seconds += 60
        minutes -= 1
    total_seconds += seconds
    seconds = 0
    total_seconds = int(total_seconds / speed)
    while total_seconds >= 3600:
        hours += 1
        total_seconds -= 3600
    while total_seconds >= 60:
        minutes += 1
        total_seconds -= 60
    while total_seconds > 0:
        seconds += total_seconds
        total_seconds = 0
    return '{:02d}:{:02d}:{:02d}'.format(hours,minutes,seconds)

