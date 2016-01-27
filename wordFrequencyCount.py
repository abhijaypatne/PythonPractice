
# for sorting dictionary based on value
import operator

# wordcount is a dictionary where,
# key = word and value is a list in which first value is frequency and
# second value is list of line numbers where the given word occurs.
# <key, value> = <word, [ frequency, line numbers]>
wordCount = {}

## To split words and count their frequency
def processLine(line, lineNumber):
    line = line.strip(" ")
    for word in line.split():
        if(wordCount.has_key(word)):       # for Python below v3.x
        #if( word in wordCount ):          # for Python V3.x and above
            wordCount.get(word)[0] += 1
            wordCount.get(word)[1].append(lineNumber)
        else:
            wordCount[word] = [1, [lineNumber]]

## Helper function to call processLine() for each line
def countWordFrequency(fileName):
    lineNumber = 0
    fd = open(fileName, "r")
    for line in fd.readlines():
        processLine(line, lineNumber)
        lineNumber += 1

## Sort according to frequency and display output
## Output format: (word, [frequency, [line numbers]])
def printOutput():
    wordCountSorted = sorted(wordCount.items(), key=operator.itemgetter(1), reverse=True)
    print 'Output format: (word, [frequency, [line numbers]])'
    for entry in wordCountSorted:
        print entry

def main():
    countWordFrequency("input.txt")
    printOutput()

if __name__=="__main__":
    main()