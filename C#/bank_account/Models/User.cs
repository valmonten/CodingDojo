using System.ComponentModel.DataAnnotations;
using System.Collections.Generic;
using System;

namespace bank_account.Models
{
    public class Users
    {
        [Key]
        public int usersid {get;set;}
        public string fname {get;set;}
        public string lname {get;set;}
        public string email {get;set;}
        public string password {get;set;}
        
    }
}