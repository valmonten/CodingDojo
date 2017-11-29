module.exports = {
    
      add: function(num1, num2) { 
           // add code here 
           var added = num1+num2;
           console.log(added);
           return added;
      },
      hello: function(){
          return console.log("Helloo")
      },
      multiply: function(num1, num2) {
           // add code here 
           ;
           return num1*num2;
      },
      square: function(num) {
           // add code here 
           return num*num;
      },
      random: function(num1, num2) {
           // add code here
           var range = Math.abs(num1-num2);
           if(num1<num2){
               var min = num1;
           }else{
               var min =num2;
           }
           
           return Math.floor(Math.random()*range)+min;
      }
    };
