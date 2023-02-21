# FrequencyAnalysis
# @FridgeTheorem
# Feb 20, 2023
def textToFreqDict(text):
    charDict = {}
    for char in text:
        charDict[char.lower()] = charDict.get(char.lower(), 0) + 1 
    return charDict

def normalizeFreqDict(freqDict):
    total = 0
    for key in freqDict:
        total += freqDict[key]
    normalizedFreqDict = {}
    for key in freqDict:
        normalizedFreqDict[key] = freqDict[key]/total
    return normalizedFreqDict


def consumeFile(file):
    with open(file, 'r') as text:
        freqDict = textToFreqDict(text)
        normalized = normalizeFreqDict(freqDict)
        sortedFreqDict = sorted(freqDict.items(), key=lambda x:x[1])
        sortedNormalized = sorted(normalized.items(), key=lambda x:x[1])
        return(sortedFreqDict, sortedNormalized)

def main():
    location = sys.argv[1]
    result = consumeFile(location)
    print("Frequency numbers: %s (Normalized: %s)" % (result[0], result[1]))
    return

if ( __name__ == "__main__" ):
    main()