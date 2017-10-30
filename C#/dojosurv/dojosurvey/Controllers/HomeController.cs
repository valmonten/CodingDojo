using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace dojosurvey.Controllers
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
        [Route("/result/")]
        public IActionResult About(string name, string location, string language, string comment)
        {
            ViewBag.name = name;
            ViewBag.location = location;
            ViewBag.language = language;
            ViewBag.comment = comment;

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
