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
    durationList = duration.split(":")
    alinanSaat = durationList[0]
    alinanDakika = durationList[1]
    alinanSaniye = durationList[2]
​
    saat = int(alinanSaat)
    dakika = int(alinanDakika)
    saniye = int(alinanSaniye)
​
    hesap = (saat * 3600 + dakika * 60 + saniye) // speed
​
    sonSaat = int((hesap // 3600))
    sonSaatStr = str(sonSaat)
    sonDakika = int(((hesap % 3600) // 60))
    sonDakikaStr = str(sonDakika)
    sonSaniye = int((hesap % 60))
    sonSaniyeStr = str(sonSaniye)
    
    if len(sonSaatStr) <= 1:
      sonSaatStrx = "0" + sonSaatStr
    else:
      sonSaatStrx = sonSaatStr
      
    if len(sonDakikaStr) <= 1:
      sonDakikaStrx = "0" + sonDakikaStr
    else:
      sonDakikaStrx = sonDakikaStr
  
    if len(sonSaniyeStr) <= 1:
      sonSaniyeStrx = "0" + sonSaniyeStr
    else:
      sonSaniyeStrx = sonSaniyeStr
    
    cevapStringi = sonSaatStrx +":"+ sonDakikaStrx +":"+ sonSaniyeStrx
      
    return cevapStringi

