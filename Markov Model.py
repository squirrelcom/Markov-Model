import random

PUNCTUATION = [".", "!", "?"]

def dollarify(wordList, k):
# Input: Takes a string as input, and a k vlaue to see how many dollar signs represent a space.
# Output: Returns a list of words in the string, and $'s in between. 

    result = []
    for l in range(k):
        result.append("$")
    for i in range(len(wordList)):
        
        if(("!" in wordList[i]) or ("." in wordList[i]) or ("?" in wordList[i]) ):
            
            result.append(wordList[i])
            for s in range(k):
                result.append("$")

        else:
            result.append(wordList[i])
    return result

def markov_model(wordList, k):
# Input:  Takes a list of words, presumably dollarify'd, and a k value to see the amount of $'s per space.
# Output:  Returns a dictionary that has the model. 

    result = {}
    check = True
    wordList = dollarify(wordList, k)
    for i in range(len(wordList) - k):
        check = True
        newList = []
        for s in range(k):
            if ((not "." in wordList[i + s]) and (not "?" in wordList[i + s]) and (not "!" in wordList[i + s])):
                newList.append(wordList[i + s])
            else: 
                check = False
                newList.append(wordList[i + s])
        newTuple = tuple(newList)
        if (check):
            if (not newTuple in result):
                result[newTuple] = [wordList[i + k]]
            else:
                result[newTuple].append(wordList[i + k])
        else:
            
            i = i + k
            
    return result



def gen_from_model(mmodel, numwords):
# Input:  Takes a model that is a dictionary of the words and there frequencies, and a number of words.
# Output:  Prints sentences based off of the amount of words in numwords.

    keys = list(mmodel.keys())
    currentKey = keys[0]
    currentWord = random.choice(mmodel[currentKey]) 
    sentence = currentWord + " "

    k = len(currentKey)

    for i in range(numwords):

        newKey = []   
        if (k == 1):
            newKey.append(currentWord)
        else:
            for s in range(k - 1):
                newKey.append(currentKey[s + 1])
            newKey.append(currentWord)        
        currentKey = tuple(newKey)

        currentWord = random.choice(mmodel[currentKey]) 
        sentence += (currentWord + " ")

        if (("." in currentWord) or ("!" in currentWord) or ("?" in currentWord)):
            currentKey = keys[0]
            currentWord = random.choice(mmodel[currentKey]) 
    print(sentence)

def markov(fileName, k, length):

# Input:  Takes a fileName to create a model from, and a k value for $'s. Length is the amount of sentences in the model.
# Output:  Prints the Length amount of sentences baed off of the markov model.
    reading = open(fileName, "r")
    inputList = reading.readlines()
    reading.close() # It's always good to close the file when you're done!
    cleanList = [x.strip("\n") for x in inputList]

    combinedList = []
    masterString = ""

    combinedList += cleanList

    for s in range(len(combinedList)):
        masterString += (combinedList[s] + " ")

    model = markov_model(masterString.split(), k)
    gen_from_model(model, length)

'''
fileName = "/Users/williamwang/Desktop/hw8pr1/testFile.txt"
markov(fileName, 2, 100)
'''
