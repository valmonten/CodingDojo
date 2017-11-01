using Microsoft.EntityFrameworkCore;

namespace quotealong.Models
{
    public class quotealongContext : DbContext
    {
        public quotealongContext(DbContextOptions<quotealongContext> options) : base(options)
        {

        }   
        public DbSet<Author> authors {get;set;}
        public DbSet<Category> category {get;set;}
        public DbSet<Meta> meta {get;set;}
    }
}