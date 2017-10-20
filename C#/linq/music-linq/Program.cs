using System;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Collections to work with
            List<Artist> Artists = JsonToFile<Artist>.ReadJson();
            List<Group> Groups = JsonToFile<Group>.ReadJson();

            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?
    var heshe = Artists.Where(Artist => Artist.Hometown== "Mount Vernon").ToList()[0];
    System.Console.WriteLine("{0} age {1}",heshe.ArtistName, heshe.Age);
            //Who is the youngest artist in our collection of artists?
        var youngest = Artists.OrderBy(Artist => Artist.Age).ToList();
    System.Console.WriteLine("{0} age {1}", youngest[0].ArtistName, youngest[0].Age);
            //Display all artists with 'William' somewhere in their real name
    var wills = Artists.Where(Artist => Artist.RealName.Contains("William")).ToList();
    foreach(var vals in wills){
        System.Console.WriteLine(vals.ArtistName);
    }

            //Display groups with names less than 8 characters in length
        var shorty = Groups.Where(Group => Group.GroupName.Length<8);
        foreach(var vals in shorty){
            System.Console.WriteLine(vals.GroupName);
        }
            //Display the 3 oldest artist from Atlanta
            var oldpeeps = Artists.Where(Artist => Artist.Hometown=="Atlanta").OrderByDescending(Artist => Artist.Age).Take(3);
            foreach(var vals in oldpeeps){
                System.Console.WriteLine(vals.ArtistName);
            }

            //(Optional) Display the Group Name of all groups that have members that are not from New York City

            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'
        }
    }
}
