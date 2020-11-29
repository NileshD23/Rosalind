def countNucFreq(seq):
    tmpFreqDict = {"A":0, "C":0, "G":0, "T":0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

#insert DNA sequence here
DNAString = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
result = countNucFreq(DNAString)
print(' '.join([str(val) for key, val in result.items()]))
      

