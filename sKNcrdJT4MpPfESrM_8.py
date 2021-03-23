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

import re
​
def remove_virus(files):
  finalList = []
  for i in re.split(r':\s', files)[1].split(", "):
    if re.search(r'\w+virus', i):
      if re.search(r'antivirus', i):
        finalList.append(i)
      elif re.search(r'notvirus', i):
        finalList.append(i)
    else:
      if re.search(r'^virus', i):
        continue
      if not re.search(r'malware', i):
        if not re.search(r'\w+malware', i):
          finalList.append(i)
  return "PC Files: " + ", ".join(finalList) if finalList else "PC Files: Empty"

