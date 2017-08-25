function sumtoone(num){
    var sum;
    while (num>9){
        sum=0;
        while(num>0){
            sum+=(num%10);
            num=Math.floor(num/10);
        }
        num=sum;

    }
    console.log(num);
    return num;
}
sumtoone(5921);



function valueatpos(num1,num2){
    var div=1;
    for(var i=1;i<=num2; i++){
        div*=10;
    }
    var value=Math.floor((num1%div)/(div/10));
    console.log(value);
    return value;
}
valueatpos(5934, 3);



function sieveoferat(num){
    var arr=[];
    var tester=2;

}