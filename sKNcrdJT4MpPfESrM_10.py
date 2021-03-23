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
    pcfiles = "PC Files:"
    viruses = ["virus", "malware"]
    notviruses = ["antivirus", "notvirus"]
    
    files = files.split()
    files.pop(0); files.pop(0)
    count = 0
    for idx, file in enumerate(files):
        if notviruses[0] in file or notviruses[1] in file:
            count += 1
            pcfiles += " "+file
        if viruses[0] in file or viruses[1] in file:
            continue
        else:
            count += 1
            pcfiles += " "+file
    if pcfiles[-1] == ",":
        pcfiles = pcfiles[:-1]
    if count == 0:
        pcfiles += " Empty"
    return pcfiles

