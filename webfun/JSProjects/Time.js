var HOUR= 8;
var MINUTE = 30;
var PERIOD = "am";




if(MINUTE>30){
    console.log("It is almost " + (HOUR+1) + PERIOD);
}
if(MINUTE<30){
    console.log("It is just past " + HOUR + PERIOD);
}
if(MINUTE=30){
    console.log("It is half past " + HOUR + PERIOD);
}