using System.ComponentModel.DataAnnotations;

namespace lost_in_the_woods.Models
{
    public abstract class BaseEntity {}
    public class Trail : BaseEntity
    {
        [Key]
        public long Id { get;set; }

        [Required]
        [MinLength(2)]
        public string TrailName { get;set; }

        [Required]
        public string Description { get;set; }

        [Required]
        public float TrailLength { get;set; }

        [Required]
        public int ElevationChange { get;set; }

        [Required]
        public float Latitude { get;set; }

        [Required]
        public float Longitude { get;set; }
        
    }
}
