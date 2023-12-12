module.exports = {

    // Exercise 1 - Iris Species Classifier
    exercise1: (SepalLen, SepalWid, PetalLen, PetalWid) => {
        if(PetalLen < 2.5){
            return ("setosa")
        }
        else{
            if(PetalWid < 1.8){
                if(PetalLen < 5 && PetalWid < 1.7){
                    return("versicolor")
                }
                else if( PetalLen<5 && !PetalWid<1.7){
                    return("virginica")
                }
                else if(!PetalLen < 5 && PetalWid >= 1.6 && SepalLen < 7 ){return ("versicolor")}
                else if(!PetalLen < 5 && PetalWid >= 1.6 && !SepalLen < 7 ){return("verginica")}
                else if(!PetalLen < 5 && !PetalWid >= 1.6 ){return("verginica")}
                
            }
            else{
                if(PetalLen<4.9 && SepalLen<6){
                    return("versicolor")
                }
                else if(PetalLen<4.9 && !SepalLen<6){return("verginica")}
                else if(!PetalLen<4.9){return("verginica")}
            }
        }
    },

    // Exercise 2 - Dog Breeds Standards
    exercise2: (breed, height, weight, male) => {
        switch(breed){
            case "Bulldog":
                if(male == true){          //Male
                    if((height <= 16.5 && height >= 13.5) && (weight <= 55 && weight >= 45) ){
                        return true
                    }
                    else{
                        return false
                    }
                }
                else{                      //Female
                    if((height <= 15.4 && height >= 12.6) && (weight <= 44 && weight >= 36) ){
                        return true
                    }
                    else{
                        return false
                    }
                }
            break;

            case "Dalmatian":
                if(male == true){
                    if((height <= 26.4 && height >= 21.6) && (weight <= 77 && weight >= 63) ){
                         return true
                    }
                    else{
                        return false
                    }
                }
                if((height <= 20.9 && height >= 17.1) && (weight <= 49.5 && weight >= 40.5) ){
                    return true
                }
                else{
                    return false
                }

            break;

            case "Maltese":
                if(male == true){
                    if((height <= 9.9 && height >= 8.1) && (weight <= 7.7 && weight >= 6.3) ){
                        return true
                    }
                    else{
                        return false
                    }
                }
                if((height <= 7.7 && height >= 6.3) && (weight <= 6.6 && weight >= 5.4) ){
                    return true
                }
                else{
                    return false
                }
            break;
        }
    },

    // Exercise 3 - Basic Statistics
    exercise3: (l) => {
        const performCalculations = (arr) => {
            var resultArray = []
            var min = Math.min.apply(null,arr)
            var max = Math.max.apply(null,arr)
            var sum = 0, avg = 0;
            var sortedArray =  arr.sort(function(a, b){return a - b});
            var arraySize = arr.length
            let middleIndex = Math.floor(arraySize / 2);
            for (var i of arr) {
                sum += i;
            }
            avg = sum / arraySize;
            let median;
            if(arraySize % 2 != 0) {         //if length is odd, return middle element
                median = sortedArray[middleIndex];
            }
            else {                         //else calculate average of central values
                median = (sortedArray[middleIndex] + sortedArray[middleIndex - 1]) / 2;
            }
            resultArray.push(min, avg, median, max)
            return resultArray
        }
        const result=[]
        var array1 =[]
        array1 = performCalculations(l)
        result.push(array1)
        var squaredArray = l.map(x => x*x);
        var array2 = performCalculations(squaredArray)
        result.push(array2)

        return result
    },


}


