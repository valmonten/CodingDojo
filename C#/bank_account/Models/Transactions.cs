using System;
using System.ComponentModel.DataAnnotations;

namespace bank_account.Models
{
    public class Transactions
    {
        [Key]
        public int transactionsid {get;set;}
        public float amount {get;set;}
        public DateTime tdate {get;set;}
        public int usersid {get;set;}
        
        
    }
}