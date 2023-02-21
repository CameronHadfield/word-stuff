# Longest Unique Lettering
# @FridgeTheorem
# Feb 20, 2023

import sys

def checkWord(word):
    lowWord = word.lower()
    if len(set(lowWord)) == len(lowWord):
        return True
    return False

def streamDictionary(dictFile):
    currMaxLen = 0
    longestPangram = ""
    with open(dictFile, 'r') as dict:
        for line in dict:
            if(checkWord(line) and len(line) > currMaxLen):
                currMaxLen = len(line)
                longestPangram = line
    return (longestPangram, currMaxLen)


def main():
    location = sys.argv[1]
    result = streamDictionary(location)
    print("Longest word with all unique letters is %s (%s char(s))" % ( result[0], result[1] ))
    return
if ( __name__ == "__main__" ):
    main()

