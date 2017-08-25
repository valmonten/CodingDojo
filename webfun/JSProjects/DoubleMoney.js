var sum=0;
var mult=.01;
for(var i=2; i<=30; i++){
    mult=mult*2;
    sum+=mult;
    console.log("The accumulated total for day "+ i +" is "+ Math.floor(sum) +" DOLLARS");
    // console.log(sum);
}