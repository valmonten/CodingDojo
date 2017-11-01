using System.ComponentModel.DataAnnotations;

namespace quotealong.Models
{
    public class QuoteViewModel : BaseEntity
    {
        [Required]
        [MinLength(8)]
        public string quote {get;set;}
        [Required]
        public int id {get;set;}
        [Required]
        public string meta {get;set;}
    }
}