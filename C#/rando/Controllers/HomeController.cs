using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace rando.Controllers
{
    public class HomeController : Controller
    {        
        private static Random random = new Random();
        public static string RandomString(int length)
        {
            const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            return new string(Enumerable.Repeat(chars, length)
            .Select(s => s[random.Next(s.Length)]).ToArray());
        }
        public IActionResult Index()
        {
            int? num = HttpContext.Session.GetInt32("num");
            if(num == null){
                HttpContext.Session.SetInt32("num", 0);
                }
            num = HttpContext.Session.GetInt32("num");
            num++;
            HttpContext.Session.SetInt32("num", (int)num);
            ViewBag.ran = RandomString(16);
            ViewBag.track = (int)HttpContext.Session.GetInt32("num");

            return View();
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
