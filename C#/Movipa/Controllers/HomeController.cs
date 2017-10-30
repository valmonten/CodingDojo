using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace Movipa.Controllers
{
    public class HomeController : Controller
    {
        [HttpPost]
        [Route("/")]
        public IActionResult Index(string title)
        {
            object[] movieinfo= new object[1];
            WebRequest.GetMovieDataAsync(title, ApiResponse =>
            {
                movieinfo.Append(ApiResponse);
            }
            ).Wait();
            object movie = movieinfo["results"[0]];
            ViewBag.movie = movie;
            
            return View();
        }

        [HttpPost]
        [Route("/query/")]
        public IActionResult query(string title)
        {
            object[] movieinfo= new object[1];
            WebRequest.GetMovieDataAsync(title, ApiResponse =>
            {
                movieinfo.Append(ApiResponse);
            }
            ).Wait();
            object movie = movieinfo["results"[0]];
            ViewBag.movie = movie;
            return RedirectToAction("Index");
        }
    }
}
