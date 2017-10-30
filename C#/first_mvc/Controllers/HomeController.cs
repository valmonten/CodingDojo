using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace first_mvc.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet]
        [Route("")]
        public string Index()
        {
            System.Console.WriteLine("Hello");
            return "Hello mundo";
        }

        public IActionResult About()
        {
            ViewData["Message"] = "Your application description page.";

            return View();
        }

        public IActionResult Contact()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult Error()
        {
            return View();
        }
    }
}
