using System;
using System.Collections.Generic;

namespace quotealong.Models
{
    public class CatQuote : BaseEntity
    {
        public int id {get;set;}
        public int quotes_id {get;set;}
        public Quote quote {get;set;}
        public int category_id {get;set;}
        public Category category {get;set;}

    }
}