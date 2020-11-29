def readFile(filePath):
    # Reading a file and returning a list of lines
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
    
def gc_content(seq):
    return round(((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)


# === Read data from the file (FASTA formatted file) ===
# Storing file contents in a list
FASTAFile = readFile("gc_content.txt")

# Dictionary for Labels + Data
FASTADict = {}

# String for holding the current label
FASTALabel = ""

# === Format, Clean, and Prepare the data ===
# Converting FASTA/List file data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

# Using Dictionary Comprehension to generate a new dictionary with GC content
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

print(RESULTDict)

# Looking for max value in values() of our new dictionary
MaxGCKey = max(RESULTDict, key = RESULTDict.get)


# === Collect Results ===
print(f'{MaxGCKey}\n{RESULTDict[MaxGCKey]}')