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
  if speed==1: return duration
  duration=duration.split(':')
  a=((int(duration[0])*3600)+(int(duration[1])*60)+int(duration[2]))/speed
  duration[0]=int(a//3600)
  duration[1]=int((a-(duration[0]*3600))//60)
  duration[2]=int(a-((duration[0]*3600)+(duration[1]*60)))
  return ':'.join([str(i).zfill(2) for i in duration])

