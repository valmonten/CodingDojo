using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace rockpaperscissors.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        [Route("/name/")]
        public IActionResult About(string name)
        {
            System.Console.WriteLine("Hi");
            
            HttpContext.Session.SetString("Username", name);
            ViewBag.oname = HttpContext.Session.GetString("Username");
            HttpContext.Session.SetInt32("won", 10);
            HttpContext.Session.SetInt32("played", 20);
            int? numberwon = HttpContext.Session.GetInt32("won");
            int? numberplayed= HttpContext.Session.GetInt32("played");
            ViewBag.won =numberwon;
            ViewBag.played = numberplayed;
            System.Console.WriteLine((int)(numberwon));
            System.Console.WriteLine("Passed");
            return View("Index");
            
        }
        [HttpPost]
        [Route("/reset/")]
        public IActionResult Contact()
        {
            HttpContext.Session.Clear();

            return View("Index");
        }

        public IActionResult Error()
        {
            return View();
        }
    }
}
