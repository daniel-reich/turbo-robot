"""


Your computer might have been infected by a virus! Create a function that
finds the viruses in `files` and removes them from your computer.

### Examples

    remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg") ➞ "PC Files: spotifysetup.exe, dog.jpg"
    
    remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ") ➞ "PC Files: antivirus.exe, cat.pdf"
    
    remove_virus("PC Files: notvirus.exe, funnycat.gif") ➞ "PC Files: notvirus.exe, funnycat.gif")

### Notes

  * Bad files will contain "virus" or "malware", but "antivirus" and "notvirus" will not be viruses.
  * Return `"PC Files: Empty"` if there are no files left on the computer.

"""

def remove_virus(files):
  files = files.split(": ")[1].split(", ")
  safe = []
  for i in range(len(files)):
    false_alarm = "antivirus" in files[i] or "notvirus" in files[i]
    if "virus" not in files[i] and "malware" not in files[i] or false_alarm:
      safe.append(files[i])
  if len(safe)==0:
    safe.append("Empty")
  return "PC Files: " + ", ".join(safe)

