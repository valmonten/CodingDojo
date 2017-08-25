// console.log('hi there');

// var num = '12';

// console.log(num);

// for(var i = 1; i <= 10; i ++) {
//     console.log(i);
// }
// let counter = 1;
// while (counter<=10) {
//     console.log(counter);
//     if(counter <5) {
//         counter += 2
//     }
//         else { counter ++; }
// }
function countdown(num){
    var array = [];
    for (var i=num; i>=0;i--){
        array.push(i);
    }
    console.log(array);
    return array;
}

countdown(-39);
