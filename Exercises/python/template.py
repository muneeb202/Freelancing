
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
