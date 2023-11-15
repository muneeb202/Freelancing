
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
