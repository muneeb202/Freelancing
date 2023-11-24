
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

# Exercise 6 - List Depth
def exercise6(l):
    depth = isinstance(l, list)
    if depth == True:
        depth = 1
    else:
        depth = 0

    while isinstance(l,list):
        for eachElement in l:
            if isinstance(eachElement,list):
                if len(eachElement) != 0:
                    l = eachElement
                depth+=1
                break
            else:
                l = eachElement
    return depth

# Exercise 7 - Change, please
def exercise7(amount,coins):
    list = [1, 2, 5, 10, 20, 50, 100, 200]
    amountInPence = amount*100

    def get_combinations(all_combs, combination, list_, current, start, end):

        if current == coins:
            if sum(combination) == amountInPence:
                all_combs.append(combination.copy())
            return
        
        if start == 8:
            return
        
        combination[current] = list_[start]

        get_combinations(all_combs, combination, list_, current + 1, start, end)
        get_combinations(all_combs, combination, list_, current, start + 1, end)


    result = []
    get_combinations(result, [0] * coins, list, 0, 0, 7)

    if len(result) == 0:
        return False
    else:
        return True

# Exercise 8 - Five Letter Unscramble
def exercise8(s):
    wordCount = 0
    allUniqueWords = set()

    def permutation(current, total_length, length, index=-1):
        if length == 0:
            allUniqueWords.add(current)
            return
        
        for i in range(total_length):
            if s.count(s[i]) == current.count(s[i]):
                continue
            permutation(current + s[i], total_length, length - 1, index + 1)

    permutation('', len(s), 5)
    path_of_file = './test_data/wordle.txt'
    wordleWords = open(path_of_file , "r").read().split('\n')
    for sequence in allUniqueWords:
        for word in wordleWords:
            if sequence == word:
                wordCount+=1
    return wordCount

# Exercise 9 - Wordle Set
def exercise9(green,yellow,gray):
    path_of_file = './test_data/wordle.txt'
    wordleWords = open(path_of_file, "r").read().split('\n')
    keyList = list(green.keys())
    yellowKeyList = list(yellow.keys())
    count = 0
    
    for eachWord in wordleWords:
        check1, check2, check3 = True, True, True
        for x in yellowKeyList:
            if x not in list(eachWord):
                check2 = False
                break
        for index, eachLetter in enumerate(eachWord):
            if eachLetter in gray:
                check1 = False
                break
            if eachLetter in yellowKeyList and index in yellow[eachLetter]:
                check2 = False
                break
            if index in keyList:
                if eachLetter != green[index]:
                    check3 = False
            if index == len(eachWord) - 1 and check1 and check2 and check3:
                count+=1

    return count

# Exercise 10 - One Step of Wordle
def exercise10(green,yellow,gray):
    def wordle(green, yellow, gray):
        path_of_file = './test_data/wordle.txt'
        wordleFile = open(path_of_file , "r")
        fileContent = wordleFile.read()
        wordleWords = fileContent.split("\n")
        keyList = list(green.keys())
        yellowKeyList = list(yellow.keys())
        count = 0
        wordle_set = []
        for eachWord in wordleWords:
            check1, check2, check3 = True, True, True
            for x in yellowKeyList:
                if x not in list(eachWord):
                    check2 = False
                    break
            for index, eachLetter in enumerate(eachWord):
                if eachLetter in gray:
                    check1 = False
                    break
                if eachLetter in yellowKeyList and index in yellow[eachLetter]:
                    check2 = False
                    break
                if index in keyList:
                    if eachLetter != green[index]:
                        check3 = False
                if index == len(eachWord) - 1 and check1 and check2 and check3:
                    wordle_set.append(eachWord)

        return wordle_set

    wordle_set = wordle(green, yellow, gray)
    for i in range(0, len(wordle_set)):
        for j in range(0, len(wordle_set)):
            if wordle_set[i] != wordle_set[j]:
                for k in range(0, 5):
                    if list(wordle_set[i])[k] == list(wordle_set[j])[k]:
                        green[k] = list(wordle_set[i])[k]
                    
                    if list(wordle_set[i])[k] != list(wordle_set[j])[k] and list(wordle_set[i])[k] in list(wordle_set[j]):
                        if list(wordle_set[i])[k] in yellow.keys() and k not in yellow[list(wordle_set[i])[k]]:
                            yellow[list(wordle_set[i])[k]].add(k)
                        else:
                            yellow[list(wordle_set[i])[k]] = {k}

                    if list(wordle_set[i])[k] != list(wordle_set[j])[k] and list(wordle_set[i])[k] not in list(wordle_set[j]):
                        if list(wordle_set[i])[k] not in gray:
                            gray.add(list(wordle_set[i])[k])
    
    def new_wordle(green, yellow, gray, wordleWords):
        keyList = list(green.keys())
        yellowKeyList = list(yellow.keys())
        
        lowest_cardinality = 0
        wordle_set = []
        for eachWord in wordleWords:
            cardinality = 0 
            for x in yellowKeyList:
                if x not in list(eachWord):
                    cardinality += 1
            for index, eachLetter in enumerate(eachWord):
                if eachLetter in gray:
                    cardinality += 1

                if eachLetter in yellowKeyList and index in yellow[eachLetter]:
                    cardinality += 1

                if index in keyList:
                    if eachLetter != green[index]:
                        cardinality += 1
                if index == len(eachWord) - 1:
                    if lowest_cardinality == 0 or lowest_cardinality > cardinality:
                        lowest_cardinality = cardinality
                    wordle_set.append([eachWord, cardinality])
        words_set = []

        for w_set in wordle_set:
            if w_set[1] == lowest_cardinality:
                words_set.append(w_set[0])
        return words_set
        
    return new_wordle(green, yellow, gray, wordle_set)
