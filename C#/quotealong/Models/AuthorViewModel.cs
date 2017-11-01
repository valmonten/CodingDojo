using System.ComponentModel.DataAnnotations;

namespace quotealong.Models
{
    public class AuthorViewmodel : BaseEntity
    {
        [MinLength(6)]
        [Required]
        public string name {get;set;}
    }
}