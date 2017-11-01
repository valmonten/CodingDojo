using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using lost_in_the_woods.Models;

namespace lost_in_the_woods.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet]
        [Route("/")]
        public IActionResult Index()
        {

            return View();
        }
        [HttpGet]
        [Route("/newtrail/")]
        public IActionResult NewTrail()
        {
            

            return View();
        }
        [HttpPost]
        [Route("/addnewtrail/")]
        public IActionResult AddNewTrail(TrailsViewModel trail)
        {
            TryValidateModel(trail);
            if(ModelState.IsValid)
            {
                // put into database
                return RedirectToAction("Index");
            }
            // throw error messages
            return RedirectToAction("NewTrail");
        }

        public IActionResult Error()
        {
            return View();
        }
    }
}
