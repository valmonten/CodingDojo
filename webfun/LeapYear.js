for(var i=0; i<=2017; i++) {
    if(i%400===0) {
        console.log(i)
        console.log("Leap Year")
    }
    else if(i%4===0){
        if(i%100!==0){
            console.log(i)
            console.log("Leap Year")

        }
        }
}