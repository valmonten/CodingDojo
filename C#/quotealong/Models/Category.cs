using System.Collections.Generic;

namespace quotealong.Models
{
    public class Category : BaseEntity
    {
        public int id {get;set;}
        public string name {get;set;}
        public List<CatQuote> catquotes {get;set;}

        public Category
    }
}