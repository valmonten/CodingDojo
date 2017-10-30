using System;
using Xunit;
using dojosurvey.Controllers;
using Microsoft.AspNetCore.Mvc;
namespace test
{
    public class UnitTest1
    {
        HomeController _hc;

        [Fact]
        public void Test1()
        {
            
        }
        public void IndexReturnsView()
        {
            var result = _hc.Index();
            Assert.IsType<ViewResult>(result);
        }

    }
}
