using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Extensions;
using quotealong.Models;


namespace quotealong.Controllers
{
    public class quotealongController : Controller
    {
        private quotealongContext _context;
        public quotealongController(quotealongContext context)
        {
            _context = context;
        }
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            ViewBag.people = _context.authors.ToList();
            ViewBag.categories = _context.category.ToList();
            return View();
        }
        [HttpPost]
        [Route("/author/add/")]
        public IActionResult AddAuthor(AuthorViewmodel incoming)
        {
            TryValidateModel(incoming);
            if(ModelState.IsValid)
            {
                System.Console.WriteLine("Gucci");
                Author newauthor = new Author();
                newauthor.name = incoming.name;
                _context.Add(newauthor);
                _context.SaveChanges();
            }else {
                System.Console.WriteLine("Noooo");
            }

            return RedirectToAction("Index");
        }
        [HttpPost]
        [Route("/quote/add")]
        public IActionResult AddQuote(QuoteViewModel incoming)
        {
            TryValidateModel(incoming);
            if(ModelState.IsValid)
            {
                Quote newquote = new Quote();
                newquote.authors_id = incoming.authorid;
                newquote.meta_id = incoming.categoryid;
                Meta newmeta = new Meta();
                CatQuote newcatquote = new CatQuote();
                
            }else{
                System.Console.WriteLine("UhhOhh");
            }
            return RedirectToAction("Index");
        }
    }
}