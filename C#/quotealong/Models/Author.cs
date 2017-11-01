using System.Collections.Generic;

namespace quotealong.Models
{
    public class Author 
    {
        public int id {get;set;}
        public string name {get;set;}
        public List<Quote> quotes {get;set;}
        public Author()
        {
            quotes = new List<Quote>();
        }
    }
}