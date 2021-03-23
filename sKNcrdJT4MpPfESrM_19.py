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
  nFile = (files.replace("PC Files:","")).split(",")
  for i in nFile:
      if i.find("virus") != -1:
          if i.find("antivirus") != -1  or i.find("notvirus") != -1:
              pass
          else:
              nFile.pop(nFile.index(i))
  for i in nFile:
      if i.find("malware") != -1:
          nFile.pop(nFile.index(i))         
  return "PC Files:" + ",".join(nFile) if len(nFile) > 0 else  'PC Files: Empty'

