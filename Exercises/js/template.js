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

    // Exercise 4 - Finite-State Machine Simulator
    exercise4: (trans, init_state, input_list) => {
        let output = []
        let out = []
        let curr = init_state + '/' + input_list[0]
        for (let inp of input_list){
            curr = curr.slice(0, 2) + inp
            out = trans[curr]
            output.push(out[2])
            curr = out
        }
        return output
    },

    // Exercise 5 - Document Stats
    exercise5: (filename) => {
        let result = []
        const {readFileSync} = require('fs');

        function syncReadFile(filename) {
        const arr = readFileSync(filename, 'utf-8');
        return arr;
        }
       
        let arr= syncReadFile("test_data/text1.txt")
        let str = arr.toString()

        //Counting number of letters
        const lettersArray= str.replace(/[^a-zA-Z]/gi,''); 
        result.push(lettersArray.length)
        
        //Counting number of numeric characters
        const numArray= str.replace(/\D/g, ''); 
        result.push(numArray.length)

        //Counting number of symbol characters
        var symbolCharCount = str.match(/[@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/g).length;
        result.push(symbolCharCount)

        //Counting number of words
        var words = str.split(/\w+/)
        var wordCount = 0
        for(w of words){
            if(w != ""){
                wordCount++;
            }
        }
        result.push(wordCount)

        
        //Counting number of sentences
        var sentences = str.split(".").filter(s => s).length;
        result.push(sentences)

        //Counting number of paragraphs
        var split_str = str.split(/\n/);
        var paragraphs = 1;
        for(x of split_str){
            if(x == "\S[\n][\n]+"){
                paragraphs++;
            }
        }
        result.push(paragraphs)
        return result
    },

    // Exercise 6 - List Depth
    exercise6: (l) => {
        let depthCount= Array.isArray(l)       //check for valid array format
        if(depthCount == true){
            depthCount = 1
        }
        else{
            depthCount = 0
        }

        while (Array.isArray(l)) {
          for (let eachElement of l) {
            if (Array.isArray(eachElement)) {
              if(Array.isArray(eachElement) && eachElement.length != 0){
                l = eachElement;
              }
              depthCount++;
              break;
            }
            else {
              l = eachElement;
            }
          }
        }
        return depthCount;
    },

    // Exercise 7 - Change, please
    exercise7: (amount,coins) => {
        let arr = [200, 100, 50, 20, 10, 5, 2, 1]
        let amountInPence = amount * 100


        const buildCombinations = (arr, num) => {
            const res = [];
            let temp, i, j, max = 1 << arr.length;
            for(i = 0; i < max; i++){
               temp = [];
               for(j = 0; j < arr.length; j++){
                for(k = 0; k < arr.length; k++){

                    if (i & 1 << j){
                        temp.push(arr[j]);
                        break
                    };
                }
               };
               if(temp.length === num){
                  res.push(temp.reduce(function (a, b) { return a + b; }));
               };
            };
            return res;
         }

        let result = buildCombinations(arr, coins)

        if (result.length == 0)
            return false
        else
            return true
    },

    
}


