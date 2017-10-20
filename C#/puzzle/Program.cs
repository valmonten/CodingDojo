using System;

namespace puzzle
{
    public class Vehicle{
        public int numPassengers;
        public double distance = 0.0;
        public Vehicle(int val){
            numPassengers = val;
        }
        public void Move(double miles){
            distance += miles;
        }
    }

    class Program
    {
        public static int[] randoray(){
            int[] inte = new int[10];
            int maxxy=0;
            int minny=26;
            int summy=0;
            Random rnd = new Random();
            for(int i=0;i<10;i++){
                inte[i]=rnd.Next(5,26);
                summy+=inte[i];
                if(inte[i]>maxxy){
                    maxxy=inte[i];
                }else if(inte[i]<minny){
                    minny=inte[i];
                }
            }

            System.Console.WriteLine("Minny is {0}, Maxxy is {1}, Summy is {2}", minny, maxxy, summy);
            return inte;
        }
        
    // Coin FlipRandom 
    
        public static string coinf(Random flip){
            string rut;
            System.Console.WriteLine("Tossing Coin!");
            int face=flip.Next(0,2);
            if(face==0){
                rut = "TAILS! You lose!";
            }else{
                rut = "HEADS! I win!!!";
            }
            System.Console.WriteLine(rut);
            return rut;
        }
        public static double tossmult(int num){
            double heads=0;
            double tails=0;
            Random flip = new Random();
            for(int i=num;i>0;i--){
                if(coinf(flip)=="HEADS! I win!!!"){
                    heads++;
                    System.Console.WriteLine("this hads");
                }
                else{
                    tails++;
                }
            }
            double horatio = heads/(heads+tails);
            System.Console.WriteLine(horatio);
            return horatio;
        }
        public static string[] name(string[] nah)
        {
            int count = 0;
            string[] newray;
            Random rng = new Random();
            int n = nah.Length;
            while (n>1){
                int k = rng.Next(n--);
                string temp = nah[n];
                nah[n] = nah[k];
                nah[k]= temp;
            }
            foreach(string val in nah){
                System.Console.WriteLine(val);
                if (val.Length>5){
                    count++;
                }
            }
            newray = new string[count];
            int idx=0;
            foreach(string val in nah){
                if (val.Length>5){
                    newray[idx]=val;
                    idx++;
                }
            }
            return newray;
        }

        static void Main(string[] args)
        {
            Vehicle car = new Vehicle(4);
            Vehicle bike = new Vehicle(1);
            Console.WriteLine(car.distance); //Prints 0
            Console.WriteLine(bike.distance); //Also Prints 0
            //The Move method however only effects the distance of the object it is referencing!!
            car.Move(70.8);
            bike.Move(97f);
            Console.WriteLine(car.distance); //Now is printing 70.8
            Console.WriteLine(bike.distance); //Still prints 0

        }
    }
}
