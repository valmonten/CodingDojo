using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace MusicApi.Controllers {

    
    public class ArtistController : Controller {

        private List<Artist> allArtists;

        public ArtistController() {
            allArtists = JsonToFile<Artist>.ReadJson();
        }
        

        //This method is shown to the user navigating to the default API domain name
        //It just display some basic information on how this API functions
        [Route("")]
        [HttpGet]
        public string Index() {
            //String describing the API functionality
            string instructions = "Welcome to the Music API~~\n========================\n";
            instructions += "    Use the route /artists/ to get artist info.\n";
            instructions += "    End-points:\n";
            instructions += "       *Name/{string}\n";
            instructions += "       *RealName/{string}\n";
            instructions += "       *Hometown/{string}\n";
            instructions += "       *GroupId/{int}\n\n";
            instructions += "    Use the route /groups/ to get group info.\n";
            instructions += "    End-points:\n";
            instructions += "       *Name/{string}\n";
            instructions += "       *GroupId/{int}\n";
            instructions += "       *ListArtists=?(true/false)\n";
            return instructions;
        }

        [Route("/artists/")]
        [HttpGet]
        public JsonResult ArtistBase() {
            return Json(allArtists);
        }

        [Route("/artists/name/{name}/")]
        [HttpGet]
        public JsonResult artistName(string name) {
            List<Artist> artist = allArtists.Where(art => art.ArtistName == name).ToList();
            return Json(artist);
        }

        [Route("/artists/realname/{name}/")]
        [HttpGet]
        public JsonResult realName(string name) {
            List<Artist> artist = allArtists.Where(art => art.RealName==name).ToList();
            return Json(artist);
        }

        [Route("/artists/hometown/{town}/")]
        [HttpGet]
        public JsonResult arthometown(string town) {
            List<Artist> artist = allArtists.Where(art => art.Hometown==town).ToList();
            return Json(artist);
        }

        [Route("/artists/groupid/{id}/")]
        [HttpGet]
        public JsonResult artingrp(int id) {
            List<Artist> artist = allArtists.Where(art => art.GroupId==id).ToList();
            return Json(artist);
        }
    }
}