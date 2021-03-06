using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace MusicApi.Controllers {
    public class GroupController : Controller {
        List<Group> allGroups {get; set;}
        public GroupController() {
            allGroups = JsonToFile<Group>.ReadJson();
        }
        [HttpGet]
        [Route("/groups/")]
        public JsonResult groups(){
            List<Group> groups = allGroups;
            return Json(allGroups);
        }

    }
}