using System;

namespace first_c
{
    class Program
    {            
        // 1 print all 1-255
            public static void print255(){
                for(int i=0; i<=255; i++){
                    System.Console.WriteLine(i);
                }
            }
        // 2 print odds
            public static void printodd255(){
                for(int i=1; i<=255; i+=2){
                    System.Console.WriteLine(i);
                }
            }
        // 3 print sum 
            public static void printsum255(){
                int summy = 0;
                for(int i=0; i<=255; i++){
                    summy+=i;
                    System.Console.WriteLine("New number: {0} sum: {1}", i, summy);
                }
            }
        // 4 Iterating an array
            public static void iteray(int[] arr){
                foreach(int val in arr){
                    System.Console.WriteLine(val);
                }
            }
        // 5 Find max in array
            public static void maxarr(int[] arr){
                int max=arr[0];
                foreach(int val in arr){
                    if(max<val){
                        max=val;
                    }
                }
                System.Console.WriteLine(max);
            }
        // 6 Get average
            public static void avgg(int[] arr){
                int summage = 0;
                int count = 0;
                foreach(int val in arr){
                    summage += val;
                    count++;
                }
                System.Console.WriteLine($"{summage/count}");
            }
        // 7 Array odd
            public static int[] arod(){
                int[] y = new int[128];
                for(int i=0; i<128; i++){
                    y[i]=((i+1)*2)-1;
                    
                }
                return y;
            }
        // 8 Greater than Y
            public static int gry(int[] arr, int y){
                int count = 0;
                foreach(int val in arr){
                    if (val>y){
                        count++;
                    }
                }
                return count;
            }
        // 9 Square Values
            public static int[] square(int[] arr){
                for(int i=0;i<arr.Length;i++){
                    arr[i]*=arr[i];
                    System.Console.WriteLine(arr[i]);
                }
                return arr;
            }
        // 10 Elimate Negative Numbers
            public static int[] elimate(int[] arr){
                for(int i=0; i<arr.Length;i++){
                    if(arr[i]<0){
                        arr[i]=0;
                    }
                    System.Console.WriteLine(arr[i]);
                }
                return arr;
            }
        // 11 Min, Max, Average
            public static void mma(int[] arr){
                int summy = 0;
                int minny = arr[0];
                int maxxy = arr[0];
                int count =0;
                foreach(int val in arr){
                    if(val>maxxy){
                        maxxy=val;
                    } else if(val<minny){
                        minny=val;
                    }
                    summy+=val;
                    count++;
                }
                System.Console.WriteLine(minny);
                System.Console.WriteLine(maxxy);
                System.Console.WriteLine($"{summy/count}");
            }
        // 12 Shifting left
            public static int[] shifty5(int[] arr){
                for(int i=0;i<arr.Length-1;i++){
                    arr[i]=arr[i+1];
                }
                arr[arr.Length-1]=0;
                return arr;
            }
        // 13 Number to string
            public static Object dojododgjing(int[] arr){
                object[] yuuup = new object[arr.Length];
                for(int i=0;i<arr.Length;i++){
                    if(arr[i]<0){
                        yuuup[i]="Dojo";
                    } else{
                        yuuup[i]=arr[i];
                    }
                    System.Console.WriteLine(yuuup[i]);
                }
                return yuuup;
            }
        static void Main(string[] args)
        {
            int[] arrayofsumshine = {1,5,4,7,8,9,-0998,78,768,31,-1234567890};
            dojododgjing(arrayofsumshine);
        }
                
        
    }
}