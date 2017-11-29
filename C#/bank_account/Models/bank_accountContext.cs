using Microsoft.EntityFrameworkCore;

namespace bank_account.Models
{
    public class bank_accountContext : DbContext
    {
        public bank_accountContext(DbContextOptions<bank_accountContext> options) : base(options)
        {}
        public DbSet<Users> users {get;set;}
        public DbSet<Transactions> transactions {get;set;}
    }
}