// 1 First function to print numbers from 1-255 WORKING

// function print1to255(){
//     for (var i=1; i<=255; i++){
//         console.log(i);
//     }

// }
// print1to255()

// 2 Next function to print integers and sums WORKING
// function intsum(){
//     var sum = 0
//     for (var i=0; i<=255; i++){
//         console.log("Int is " + i);
//         sum += i;
//         console.log("Sum is " + sum);
//     }
// }
// intsum()

// 3 Find and Print Max WORKING

// function arraymax(arr){
//     max = -9000
//     for (var i=0; i<arr.length; i++){
//         if(arr[i]>max){
//             max=arr[i];
//         }
//     }
//     console.log(max)
// }
// arraymax([7, 2, 5, 2, 7, 92, 1829, 442, 2901, 9000, 3985])

// 4 Array with Odds WORKING

// function oddarray(){
//    var arr=[]
//     for(var i=1; i<=255; i+=2){
//         arr.push(i);
//     }
//     console.log(arr)
// }
// oddarray();

// 5 Greater than Y WORKING
// function greaterthany(arr, y){
//     var count=0
//     for(var i=0; i<arr.length; i++){
//         if(arr[i]>y){
//         count++
//         }

//     }
//     console.log(count)
// }
// greaterthany([7, 2, 5, 4, 3, 1, 8, 9], 7)

// 6 Max Min Average WORKING
// function maxminavg(arr){
//     var max= -Infinity;
//     var min= Infinity;
//     var sum=0;
//     for(var i=0; i<arr.length; i++){
//         if (arr[i]>max){
//             max=arr[i];
//         }
//         if (arr[i]<min){
//             min=arr[i];
//         }
//         sum+=arr[i];
//     }
//     var avg= sum/arr.length;
//     console.log("Max is " + max);
//     console.log("Min is " + min);
//     console.log("Avg is " + avg);
// }
// maxminavg([5, 7, 9, 11, 13]);

// 7 Swap String for Array Negative Values WORKING
// function swapneg(arr){
//     for(var i=0; i<arr.length; i++){
//         if(arr[i]<0){
//             arr[i]= "Dojo";
//         }
//     }
//     console.log(arr);
// }
// swapneg([-6, 5, -4, 3, -2]);

// 8 Print odds WORKING
// function printodds(){
//     for(var i=1; i<=255; i+=2){
//         console.log(i);
//     }
// }
// printodds()

// 9 Iterate and Print Array
// function printarray(arr){
//     console.log(arr);
// }
// printarray([2, 4, 24, 7]);

// 10 Get and Print Average WORKING
// function arravg(arr){
//     var sum=0
//     for(var i=0; i<arr.length; i++){
//         sum+=arr[i];
//     }
//     var avg = sum/arr.length;
//     console.log(avg)

// }
// arravg([1, 2, 3, 4]);

// 11 Square Values WORKING
// function sqrarr(arr){
//     for(var i=0; i<arr.length; i++){
//         arr[i]*=arr[i];
//     }
//     console.log(arr);
// }
// sqrarr([4, 5, 7]);

// 12 Zero Out Negative Numbers
// function zeronegs(arr){
//     for(var i=0; i<arr.length; i++){
//         if(arr[i]<0){
//             arr[i]=0;
//         }
//     }
//     console.log(arr);
// }
// zeronegs([3, -1, -9, 4, 5]);

// 13 Shift Array Values WORKING
// function shiftleft(arr){
    
//     for(var i=0; i<arr.length; i++){
//         arr[i]=arr[i+1];
        
//     }
//     arr[arr.length-1]=0;
//     console.log(arr);
// }
// shiftleft([7, 4, 3, 2, 1]);