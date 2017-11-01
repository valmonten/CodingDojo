using System;
using System.Collections.Generic;

namespace quotealong.Models
{
    public class Quote : BaseEntity
    {
        public int id {get;set;}
        public string quote {get;set;}
        public int authors_id {get;set;}
        public Author author {get;set;}
        public int meta_id {get;set;}
        public Meta meta {get;set;}
        public List<CatQuote> catquotes {get;set;}

        public Quote()
        {
            catquotes = new List<CatQuote>();
        }

    }
}