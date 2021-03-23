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

def dna_to_rna (dna):
  dic = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
  return ''.join([dic[char] for char in dna if char in dic])

