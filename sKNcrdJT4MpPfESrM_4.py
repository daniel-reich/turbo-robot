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
  lst = files[10:].split(", ")
  new = []
  for i in lst:
    if i == "notvirus.exe" or i == "antivirus.exe":
      new.append(i)
      continue
    if "virus" in i or "malware" in i:
      continue
    new.append(i)
  if len(new) < 1:
    new.append("Empty")
  return files[:10] + ", ".join(new)

