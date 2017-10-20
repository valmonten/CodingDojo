using System;

namespace Wizard__Ninja__Samurai
{
    public class Enemy : Player{

    //The { get; set; } format creates accessor methods for the field specified
    //This is done to allow flexibility
    public int strength { get; set; }
    public int intelligence { get; set; }
    public int dexterity { get; set; }
    public int maxhealth { get; set; }
    public Enemy(string person) : base()
    {
        name = person;
        strength = 3;
        intelligence = 3;
        dexterity = 1;
        health = 100;
        maxhealth = 100;
        location = 10;
        System.Console.WriteLine("An eeriness creeps over the land.");
    }
}

    public class Zombie : Enemy{
        public Zombie(string thingy) : base(thingy){
            System.Console.WriteLine("Oh no! {0} is a zombie!",thingy);
            name= thingy;
        }
        public void bite(object who){
            Human victim = who as Human;
            if(victim == null){
                System.Console.WriteLine("Zombie bite failed!");
            }else{
                victim.health-=24;
                System.Console.WriteLine("{2} bit {0}! {0} has {1} health left!", victim.name,victim.health,name);
            }

        }
        public void turn(Player[][] playerss){
            if(playerss[0][2].health>0){
                bite(playerss[0][2]);
                if(playerss[0][2].health<0){
                    Zombie Noname = new Zombie("Noname");
                    playerss[1][3]=Noname;
                }
            }
            else if(playerss[0][1].health>0){
                bite(playerss[0][1]);
                if(playerss[0][1].health<0){
                    Zombie Sam = new Zombie("Sam");
                    playerss[1][2]=Sam;
                }
            }
            else{
                bite(playerss[0][0]);
                if(playerss[0][0].health<0){
                    System.Console.WriteLine("Game OVER!!! YOU JOINED THE ZOMBIE PLAGUE!");
                }
            }
            
        }
        }

    }
