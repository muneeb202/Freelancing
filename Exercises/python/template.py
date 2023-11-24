
# Exercise 1 - Iris Species Classifier
def exercise1(SepalLen,SepalWid,PetalLen,PetalWid):
    if PetalLen < 2.5:
        return("setosa")
    else:
        if PetalWid < 1.8:
            if PetalLen < 5 and PetalWid < 1.7:
                return("versicolor")
            elif PetalLen < 5 and not PetalWid < 1.7:
                return("virginica")
            elif not PetalLen < 5 and PetalWid >=1.6 and SepalLen < 7:
                return("versicolor")
            elif not PetalLen < 5 and PetalWid >= 1.6 and not SepalLen < 7:
                return("virginica")
            elif not PetalLen < 5 and not PetalWid >= 1.6:
                return("virginica")
        else:
            if PetalLen < 4.9 and SepalLen < 6:
                return("versicolor")
            elif PetalLen < 4.9 and not SepalLen < 6:
                return("virginica")
            elif not PetalLen < 4.9:
                return("virginica")

# Exercise 2 - Dog Breeds Standards
def exercise2(breed,height,weight,male):
    if breed == "Bulldog":
        if male == True:
            if (height <= 16.5 and height >= 13.5) and (weight <= 55 and weight >= 45):
                return True
            else:
                return False
        else:
            if (height <= 15.4 and height >= 12.6) and (weight <= 44 and weight >= 36):
                return True
            else:
                return False

    elif breed == "Dalmatian":
        if male == True:
            if (height <= 26.4 and height >= 21.6) and (weight <= 77 and weight >= 63):
                return True
            else:
                return False
        else:
            if (height <= 20.9 and height >= 17.1) and (weight <= 49.5 and weight >= 40.5):
                return True
            else:
                return False

    elif breed == "Maltese":
        if male == True:
            if (height < 9.9 and height > 8.1) and (weight < 7.7 and weight > 6.3):
                return True
            else:
                return False
        else:
            if (height < 7.7 and height > 6.3) and (weight < 6.6 and weight > 5.5):
                return True
            else:
                return False

# Exercise 3 - Basic Statistics
def exercise3(l):
    def performCalculations(list_):
        resultList = []
        minimum = min(list_)
        maximum = max(list_)
        copylist = list_.copy()
        copylist.sort()
        length = len(list_)
        if length % 2 == 0:
            median = (copylist[length//2] + copylist[(length // 2) - 1]) / 2
        else:
            median = copylist[length//2]
        average = sum(list_) / length
        resultList.extend([minimum, average, median, maximum])
        return resultList

    result = []
    list1 = []
    list1 = performCalculations(l)
    result.append(tuple(list1))
    squaredList = [num**2 for num in l]
    list2 = performCalculations(squaredList)
    result.append(tuple(list2))
    return result

# Exercise 4 - Finite-State Machine Simulator
def exercise4(trans,init_state,input_list):
    output = []
    curr = init_state + '/' + input_list[0]               # start state + 1st input

    for inp in input_list:
        curr = curr[0:2] + inp                           # current state + current input
        out = trans.get(curr)                                   # get value of current_state/current_input
        output.append(out[2:])                                       # append output to list

        curr = out                                           # change state

    return output

# Exercise 5 - Document Stats
def exercise5(filename):
    result = []
    wordleFile = open(filename , "r")
    fileContent = wordleFile.read()

    #Counting letters
    letterCount = 0
    for eachWord in fileContent:
        for eachLetter in eachWord:
            if eachLetter.isalpha():
                letterCount+=1

    result.append(letterCount)

    #Counting numeric characters
    numericCount = 0
    for eachWord in fileContent:
        for eachLetter in eachWord:
            if eachLetter.isdigit():
                numericCount+=1

    result.append(numericCount)

    #Counting symbol characters
    symbolCount = 0
    specialChars = "!\"£$%&/()='?^+*[]{}#@-_.:,;" 
    for eachWord in fileContent:
        for eachLetter in eachWord:
            if any((c in specialChars) for c in eachLetter):
                symbolCount+=1

    result.append(symbolCount)

    #Counting words
    wordCount = 0
    allchars = specialChars + " \n\t"

    for totalword in fileContent.split():
        word = ''
        for ch in totalword:
            if ch in allchars:
                if word != '':
                    wordCount += 1
                    word = ''
            else:
                word += ch
        if word != '':
            wordCount += 1

    result.append(wordCount)

    #Counting sentences
    sentenceCount = 0
    for eachWord in fileContent:
        for eachLetter in eachWord:
            if eachLetter == "." or eachLetter == "!" or eachLetter == "?":
                sentenceCount+=1

    result.append(sentenceCount)

    #Counting paragraphs
    fileLines = []
    with open(filename) as my_file:
        fileLines = my_file.readlines()

    paragraphCount = 0
    with open(filename) as f:
        for i, l in enumerate(f):
            if l.isspace() and len(fileLines[i+1])-1 != 0:
                paragraphCount+=1

    result.append(paragraphCount+1)
    return tuple(result)

