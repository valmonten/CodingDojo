using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using logreg.Models;
using DbConnection;
using Microsoft.AspNetCore.Http;

namespace logreg.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet]
        [Route("/")]
        public IActionResult Index()
        {
            ViewBag.errors = ModelState.Values;
            return View();
        }
            
        
        [HttpPost]
        [Route("/create/")]
        public IActionResult About(Register model)
        {
            ViewBag.errors = ModelState.Values;
            if(ModelState.IsValid){
                try
                {                    
                    DbConnector.Execute($"INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES ('{model.FirstName}', '{model.LastName}', '{model.Email}', '{model.Password}', NOW(), NOW())");
                }
                catch
                {
                    ViewBag.duplicate = "That email already exists";
                    return View("Index"); 
                }

                return RedirectToAction("Contact");
            }
            
            return View("Index");
        }
        [HttpGet]
        [Route("/loginland/")]
        public IActionResult Contact()
        {

            return View();
        }
        [HttpPost]
        [Route("/login/")]
        public IActionResult Login(Login user)
        {
            List<Dictionary<string, object>> match = DbConnector.Query($"SELECT * FROM users WHERE email='{user.Email}' and password='{user.Password}'");
            if(match.Count>0)
            {
            object firstemail = match[0]["email"];
            object firstid = match[0]["id"];
            object firstname = match[0]["first_name"];
            HttpContext.Session.SetString("logname", $"{firstname}");
            HttpContext.Session.SetInt32("logid", (int)firstid);
            HttpContext.Session.SetString("logemail", $"{firstemail}");
            return RedirectToAction("Success");
            }
            else
            {
                ViewBag.loginerror = "That email and password combo does not exist";
            }
            return View("Contact");
        }
        [HttpGet]
        [Route("/success/")]
        public IActionResult Success()
        {
            List<Dictionary<string, object>> messages = DbConnector.Query("SELECT * FROM messages");
            ViewBag.messages = messages;
            ViewBag.name = HttpContext.Session.GetString("logname");
            return View();
        }
        [HttpPost]
        [Route("/addmessage/")]
        public IActionResult Addmessage(string message)
        {
            DbConnector.Execute($"INSERT INTO messages (message, created_at, updated_at) VALUES ('{message}', NOW(), NOW())");
            return RedirectToAction("Success");
        }
        [HttpGet]
        [Route("/logoff/")]
        public IActionResult Logoff(){
            HttpContext.Session.Clear();
            return RedirectToAction("Contact");
        }
    }
}
