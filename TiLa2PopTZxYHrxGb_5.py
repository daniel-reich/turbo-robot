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

class Time:
  
  def get_seconds(time):
    hours, mins, secs = [int(i) for i in time.split(':')]
    secs += int(hours * 3600)
    secs += int(mins * 60)
    
    return secs
  
  def update_time_speed(seconds, speed_rate):
    return seconds // speed_rate
  
  def get_hours_mins_secs(seconds):
    hours = str(int(seconds // 3600))
    seconds = seconds % 3600
    mins = str(int(seconds // 60))
    seconds = str(int(seconds % 60))
    
    while len(hours) < 2:
      hours = '0' + hours
    while len(mins) < 2:
      mins = '0' + mins
    while len(seconds) < 2:
      seconds = '0' + seconds
    
    return ':'.join([hours, mins, seconds])
​
def playback_duration(duration, speed):
  
  seconds = Time.get_seconds(duration)
  updated = Time.update_time_speed(seconds, speed)
  print(seconds, updated)
  return Time.get_hours_mins_secs(updated)

