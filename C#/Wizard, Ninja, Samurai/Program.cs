using System;

namespace Wizard__Ninja__Samurai
{
    public class Player{
        public int location { get; set; }
        public int health { get; set; }
        public string name;
        public void turn(){

        }
        public Player(){
            health = 0;
        }

    }
    public class Human : Player
{
    //The { get; set; } format creates accessor methods for the field specified
    //This is done to allow flexibility

    public int strength { get; set; }
    public int intelligence { get; set; }
    public int dexterity { get; set; }
    public int maxhealth { get; set; }
    public Human(string person) : base()
    {
        name = person;
        strength = 3;
        intelligence = 3;
        dexterity = 3;
        health = 100;
        maxhealth = 100;
        location = 0;
    }
    public Human(string person, int str, int intel, int dex, int hp) : base()
    {
        name = person;
        strength = str;
        intelligence = intel;
        dexterity = dex;
        health = hp;
        maxhealth=100;
        location = 0;
    }
    public void attack(object obj)
    {
        Player enemy = obj as Player;
        if(enemy == null)
        {
            Console.WriteLine("Failed Attack");
        }
        else
        {
            int dmg = strength*5;
            enemy.health -= dmg;
            System.Console.WriteLine("{0} was attacked by {3} for {1} health!, {0} has {2} health left",enemy.name,dmg,enemy.health,name);
        }
    }
}
    public class Wizard : Human{
        
        public Wizard(string person) : base(person, 1, 25, 2, 50){
            System.Console.WriteLine("You are a wizard {0}", person);
            maxhealth = 50;
        }
        
        public void heal(){
            int incr = 10*intelligence;
            health += incr;
            if(health>maxhealth){
                health=maxhealth;
            }
            System.Console.WriteLine("{2} healed {0} health points. {2} is at {1} health.",incr,health,name);
        }
        public void fireball(object obj){
            Player enemy = obj as Player;
            if(enemy == null){
                System.Console.WriteLine("Your fireball failed");
            }
            else{
                Random rand = new Random();
                int dmg =rand.Next(20,50);
                enemy.health-=dmg;
                System.Console.WriteLine("{3} did {0} damage. {1}'s remaining health is {2}", dmg,enemy.name,enemy.health,name);
            }
        }
        public void turn(Player[][] playerss){
            System.Console.WriteLine("Defend yourself! Fireball or heal?!");
            string encounter1 = Console.ReadLine();
            if(encounter1 == "FIREBALL" || encounter1 == "heal" || encounter1=="Heal"){
                System.Console.WriteLine("Who do you want to fireball?");
                var e12 = Console.ReadLine();
                
                if(e12 == "sam"|| e12== "Sam"|| e12 == "NONAME" || e12=="bie" || e12=="Bie"){
                    System.Console.WriteLine("Noname you said?");
                    this.fireball(playerss[0][2]);
                    if(playerss[0][2].health<0){
                            Player Noname = new Player();
                            playerss[0][2]=Noname;
                            System.Console.WriteLine("Noname is dead");
                        
                    }
                
                }
                else if(e12 == "noname"|| e12== "Noname"|| e12 == "SAM" || e12=="Zom"||e12=="zom"){
                    System.Console.WriteLine("Sam you said?");
                    this.fireball(playerss[0][1]);
                    if(playerss[0][1].health<0){
                        Player Sam = new Player();
                        playerss[0][1]=Sam;
                        System.Console.WriteLine("Sam is dead");
                    //enamyturn
                    }
                }
                else if(e12=="BIE"){
                    this.fireball(playerss[4]);
                    if(playerss[1][1].health<0){
                        Player bie = new Player();
                        playerss[1][1]=bie;
                        System.Console.WriteLine("bie is dead");
                    //enemyturn
                    }
                }
                else if(e12=="ZOM"){
                    this.fireball(playerss[3]);
                    if(playerss[1][0].health<0){
                        Player zom = new Player();
                        playerss[1][0]=zom;
                        System.Console.WriteLine("zom is dead");
                    //enemyturn
                    }
                }

            }else if (encounter1 == "HEAL" || encounter1 == "fireball" || encounter1=="Fireball"){
                System.Console.WriteLine("Whats that? heal?");
                this.heal();
            }
            else{
                System.Console.WriteLine("Sorry I dont understand what that means. Try again?");
                turn(playerss);
            }
        }
    }
    public class Ninja : Human{
        public Ninja(string person) : base(person,3,3,175,50){
            System.Console.WriteLine("The ninja by the name of {0} was stealthily born in a puff of smoke",person);
        }
        public void steal(object obj){
            Human enemy = obj as Human;
            if(enemy == null){
                System.Console.WriteLine("Steal failed!");
            }
            else{
                int dmg=strength*5;
                enemy.health-=dmg;
                health+=10;
                if(health>maxhealth){
                    health=maxhealth;

                }
                System.Console.WriteLine("{0} stole healing pots from {1}, and healed for 10 health! {0}'s health is now {2} and {1}'s health is now {3}",name,enemy.name,health,enemy.health);
            }
        }
        public void get_away(){
            health-=15;
            System.Console.WriteLine("{0} Escaped in a cloud of smoke! His health is now {1}",name,health);
        }
        public void turn(Player[][] playerss){
            if(playerss[1][0].health>0){
            this.attack(playerss[1][0]);
                if(playerss[1][0].health<=0){
                    Player zom = new Player();
                    playerss[1][0]=zom;
                }
            }
            else if(playerss[1][1].health>0){
                this.attack(playerss[1][1]);
                Player bie = new Player();
                playerss[1][1]=bie;
            }

        }
        
    }
    public class Samurai : Human{
        public int how_many =0;
        public Samurai(string person) : base(person){
            maxhealth=100;
            health=100;
            how_many++;
            System.Console.WriteLine("An honorable samurai named {0} marches forth looking like he is ready to do battle.",person);
        }
        public void death_blow(object obj){
            Human enemy = obj as Human;
            if(enemy==null){
                System.Console.WriteLine("{0}'s Death Blow failed!",name);
            }
            else{
                if(enemy.health<50){
                    enemy.health=0;
                    System.Console.WriteLine("Death Blow from {0} killed {1}",name,enemy.name);
                }
                else{
                    System.Console.WriteLine("{0}'s Death Blow failed because {1}'s health was too high!", name,enemy.name);
                }
            }
        }
        public void meditate(){
            health=maxhealth;
            System.Console.WriteLine("{0} Healed to max health through meditation!",name);
        }
        public void turn(Player[][] playerss){
            if(playerss[1][1].health>0){
                this.attack(playerss[1][1]);
                if(playerss[1][1].health<=0){
                    Player zom = new Player();
                    playerss[1][1]=zom;
                }
            }
            else if(playerss[1][0].health>0){
                this.attack(playerss[1][0]);
                if(playerss[1][0].health<=0){
                    Player zom = new Player();
                    playerss[1][0]=zom;
                }
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            System.Console.WriteLine("Do you wanna play? (Yes/No)");
            string InputLine = Console.ReadLine();


            if(InputLine == "Yes" || InputLine == "yes" || InputLine == "y" || InputLine == "Y"){
                System.Console.WriteLine("Let's do it!");
                System.Console.WriteLine("What is your name?");
                Console.ReadLine();
                System.Console.WriteLine("Sorry, what was that? Can you speak up? I'm hard of hearing.");
                string username = Console.ReadLine();
                System.Console.WriteLine("Harry you said? Great, come right this way. My name is Skip and I'll be your guide for this journey. Let me introduce your to your allies.");



                System.Console.WriteLine("By the way Harry, Are you a wizard, samurai, or ninja?", username);
                string wsn = Console.ReadLine();


                // if(wsn== "Wizard" || wsn=="wizard"){

                // }else if(wsn == "Samurai" || wsn=="samurai"){
                //     Samurai player = new Samurai(username);   
                // }else if (wsn == "ninja" || wsn== "Ninja"){
                //     Ninja player = new Ninja(username);
                // }
                System.Console.WriteLine("Whats that? Wizard you said? Ah yes,");
                Console.ReadLine();

                    Wizard Harry = new Wizard("Harry");
                    System.Console.WriteLine("Great lets get started. First of all meet your allies: Sam the samurai and Noname the ninja");
                    Console.ReadLine();
                    Samurai Sam = new Samurai("Sam");
                    Console.ReadLine();
                    Ninja Noname = new Ninja("Noname");
                    Console.ReadLine();
                    System.Console.WriteLine("Be careful! There are evil monsters abound!");
                    Console.ReadLine();
                    Zombie zom = new Zombie("zom");
                    Console.ReadLine();
                    Zombie bie = new Zombie("bie");
                    Console.ReadLine();
                    Player[][] playerss = new Player[2][];
                    Player[] allies = new Player[3];
                    Player[] enemies = new Player[4];
                    playerss[0]= allies;
                    playerss[1]=enemies;
                    playerss[0][0]=Harry;
                    playerss[0][1]=Sam;
                    playerss[0][2]=Noname;
                    playerss[1][0]=zom;
                    playerss[1][1]=bie;

                    // while(playerss[0][0].health>0 || (playerss[1][0].health>0 || playerss[1][0].health>0))
                    Harry.turn(playerss);
                    zom.turn(playerss);
                    Sam.turn(playerss);
                    bie.turn(playerss);
                    Noname.turn(playerss);
                    Harry.turn(playerss);

                


                



                
            }
            else
            {
                System.Console.WriteLine("Ok. Bye!");
            }

        }
    }
}
