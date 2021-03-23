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

from math import floor
string = lambda x: '0' + str(x) if x < 10 else str(x)
def playback_duration(duration, speed):
  time = duration.split(':');
  seconds = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
  seconds /= speed
  hours = floor(seconds / 3600)
  seconds -= 3600 * hours
  minutes = floor(seconds / 60)
  seconds -= 60 * minutes
  seconds = floor(seconds)
  return '{}:{}:{}'.format(string(hours),string(minutes),string(seconds))

