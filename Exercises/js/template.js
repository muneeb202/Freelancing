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

}


