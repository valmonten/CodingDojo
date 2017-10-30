using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace starwars.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet]
        [Route("/")]
        public IActionResult Index()
        {
            return View();
        }
        [HttpPost]
        [Route("/process/")]
        public IActionResult About(string query)
        {
            System.Console.WriteLine("Here");
            var person = new Dictionary<string, object>();
            WebRequest.GetDataAsync(query, ApiResponse =>
            {
                person = ApiResponse;
            }
            ).Wait();
            System.Type type = person.GetType();
            System.Console.WriteLine(type);
            System.Console.WriteLine(person);
            System.Console.WriteLine("Stop");
            return RedirectToAction("Index");
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
