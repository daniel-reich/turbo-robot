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
  hour, minute, second = map(int, duration.split(":"))
  total = hour*3600 + minute*60 + second
  total /= speed
  hours = int(total // 3600)
  total -= hours*3600
  minutes = int(total // 60)
  total -= minutes*60
  seconds = int(total)
  return "{:0>2}:{:0>2}:{:0>2}".format(hours, minutes, seconds)

