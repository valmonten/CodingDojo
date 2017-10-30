using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using lost_in_the_woods.Factory;

namespace lost_in_the_woods.Controllers
{
    public class HomeController : Controller
    {
        private readonly TrailFactory userFactory;
        public HomeController()
        {
            userFactory = new UserFactory();
        }
        [HttpGet]
        [Route("/")]
        public IActionResult Index()
        {
            return View();
        }
        [HttpGet]
        [Route("/addtrail/")]
        public IActionResult About()
        {
            

            return View();
        }
        [HttpPost]
        [Route("/addingtrail/")]
        public IActionResult Contact()
        {

            return RedirectToAction("Index");
        }

        public IActionResult Error()
        {
            return View();
        }
    }
}
