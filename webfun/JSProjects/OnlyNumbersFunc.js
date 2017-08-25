// var newArray = numbersOnly([1, "apple", -3, "orange", 0.5]);

function onlynumber(arr){
    var newarray =[]
    for(var i=0; i<arr.length; i++){
        if(typeof arr[i]==='number'){
            newarray.push(arr[i]);

        }
    }
    console.log(newarray);
}
onlynumber([1, "apple", -3, "orange", 0.5])