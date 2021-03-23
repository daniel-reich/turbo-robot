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
  A=duration.split(':')
  ts=int((int(A[0])*3600+int(A[1])*60+int(A[2]))/speed)
  h,r1=divmod(ts, 3600)
  m,s=divmod(r1, 60)
  H=str(h).zfill(2) if h<100 else str(h)
  M=str(m).zfill(2)
  S=str(s).zfill(2)
  return '{}:{}:{}'.format(H,M,S)

