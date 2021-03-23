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
  hours = int(duration.split(":")[0])
  minutes = int(duration.split(":")[1])
  seconds = int(duration.split(":")[2])
  time = hours*3600 + minutes*60 + seconds
  time = time/speed
  new_hours = int(time/3600)
  if new_hours < 10:
    str_new_hours = "0" + str(new_hours)
  else:
    str_new_hours = str(new_hours)
  new_minutes = int((time-new_hours*3600)/60)
  if new_minutes  == 0:
    str_new_minutes = "00"
  else:
    str_new_minutes = str(new_minutes)
  new_seconds = int(time-new_hours*3600 - new_minutes*60)
  if new_seconds == 0:
    str_new_seconds = "00"
  else:
    str_new_seconds = str(new_seconds)
  return ("{0}:{1}:{2}".format(str_new_hours, str_new_minutes, str_new_seconds))

