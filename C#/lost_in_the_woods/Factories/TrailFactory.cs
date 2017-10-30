using System.Collections.Generic;
using System.Linq;
using Dapper;
using System.Data;
using MySql.Data.MySqlClient;
using lost_in_the_woods.Models;
 
namespace lost_in_the_woods.Factory
{
    public class UserFactory : IFactory<Trail>
    {
        private string connectionString;
        public UserFactory()
        {
            connectionString = "server=localhost;userid=root;password=root;port=8889;database=mydb;SslMode=None";
        }
        internal IDbConnection Connection
        {
            get {
                return new MySqlConnection(connectionString);
            }
        }
                public void Add(Trail item)
        {
            using (IDbConnection dbConnection = Connection) {
                string query =  "INSERT INTO trails (TrailName, , password, created_at, updated_at) VALUES (@Name, @Email, @Password, NOW(), NOW())";
                dbConnection.Open();
                dbConnection.Execute(query, item);
            }
        }
        public IEnumerable<Trail> FindAll()
        {
            using (IDbConnection dbConnection = Connection)
            {
                dbConnection.Open();
                return dbConnection.Query<Trail>("SELECT * FROM trails");
            }
        }
        public Trail FindByID(int id)
        {
            using (IDbConnection dbConnection = Connection)
            {
                dbConnection.Open();
                return dbConnection.Query<Trail>("SELECT * FROM users WHERE id = @Id", new { Id = id }).FirstOrDefault();
            }
        }
    }
}