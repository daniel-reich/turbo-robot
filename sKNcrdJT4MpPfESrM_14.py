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
  files = files[10:]
  print(files)
  l = list()
  for elt in files.split(', '):
    if "virus" not in elt and "malware" not in elt:
      l.append(elt)
    if "antivirus" in elt or "notvirus" in elt:
      l.append(elt)
  
  s = 'PC Files: '
  for elt in l:
    s += elt + ", "
    
  if len(l) == 0:
    return s + "Empty"
    
  return s[:-2]

