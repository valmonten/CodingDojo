var birthdaycountdown = 60;
for(i=birthdaycountdown; i>=0;i--){
    if(i>=30){
        console.log("Sad face, your birthday is "+ i + " days away.");
    }
    else if(i<5 && i!==0){
        console.log("LIKE OMG THERE IS A SURPRISE COMING IN " + i + " DAYS!");
    }
    else if(i<30 && i!==0){
        console.log("Yay! Your birthday is " + i + " days away!")
    }
    else{
        console.log("HAPPY BIRTHDAY! SURPRISE YOUR PETTING ZOO IS HERE!")
    }
}