"""


Transcribe the given DNA strand into corresponding mRNA - a type of RNA, that
will be formed from it after transcription. DNA has the bases A, T, G and C,
while RNA converts to U, A, C and G respectively.

### Examples

    dna_to_rna("ATTAGCGCGATATACGCGTAC") ➞ "UAAUCGCGCUAUAUGCGCAUG"
    
    dna_to_rna("CGATATA") ➞ "GCUAUAU"
    
    dna_to_rna("GTCATACGACGTA") ➞ "CAGUAUGCUGCAU"

### Notes

  * Transcription is the process of making complementary strand.
  * A, T, G and C in DNA converts to U, A, C and G respectively, when in mRNA.

"""

def dna_to_rna(dna):
  rna = ""
  for i in dna:
    if i == "A":
      rna = rna + "U"
    if i == "T":
      rna = rna + "A"
    if i == "G":
      rna = rna + "C"
    if i == "C":
      rna = rna + "G"
  return rna

