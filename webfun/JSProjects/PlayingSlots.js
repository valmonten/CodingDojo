function gamble(tokens){

    if(tokens==0){
        console.log("You ran out of money =(");
    } else{    
        while(tokens>=1){

            tokens--;        

            if(Math.floor(Math.random()*100)==55){
                
                tokens+=(Math.floor((Math.random()*50)+50));

                console.log("DING DING DING YOU WON! You have " + tokens + " left.");
            } else {
                console.log("Nope, Try Again. You have " + tokens + " left.");
            }      
        }      
    }
}
gamble(100);