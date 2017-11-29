class Card
{
    constructor(suit, value, vname)
    {
        this.suit = suit;
        this.value = value;
        this.vname = vname;
    }
}

class Deck
{

    constructor(){
        //add 52 unique cards
        this.suits = ["Spade", "Club", "Heart", "Diamond"];
        this.value = {"Ace":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen": 12, "King":13}
        this.cardarray = [];
        for(let i =0;i<this.suits.length;i++){
            for(var key in this.value){
                let newcard = new Card(this.suits[i], this.value[key], key);
                this.cardarray.push(newcard);
            }
        }
        console.log("Fresh deck of 52 cards made!")
    }
    shuffle(){
        for(let i=0; i<52; i++)
        {
            let randy = Math.ceil(Math.random()*52);
            let holder = this.cardarray[i];
            this.cardarray[i] = this.cardarray[randy];
            this.cardarray[randy] = holder;
        }
        
    }

}

let playingcards = new Deck();
console.log(playingcards.cardarray[2]);
playingcards.shuffle();
console.log(playingcards.cardarray[2]);