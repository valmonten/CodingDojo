using System.ComponentModel.DataAnnotations;
using DbConnection;

namespace logreg.Models
{
    public class Register
    {
        [Required]
        [MinLength(2)]
        public string FirstName { get; set;}
        [Required]
        [MinLength(2)]
        public string LastName { get; set;}
        [Required]
        [EmailAddress]
        public string Email { get;set; }
        [Required]
        [MinLength(8)]
        public string Password { get;set; }
        [Required]
        [Compare("Password", ErrorMessage = "Passwords must match")]
        public string ConfirmPassword { get;set; }        
    }
    public class Login
    {
        [Required]
        public string Email { get;set; }
        [Required]
        public string Password { get;set; }
    }
}