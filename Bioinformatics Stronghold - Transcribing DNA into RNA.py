def transcription(seq):
    # DNA --> RNA Transcription
    return seq.replace("T", "U")

print(transcription("GATGGAACTTGACTACGTAAATT"))