from django.db import models

class Job(models.Model):
    """
    A model to represent a job listing.
    """
    EXPERIENCE_CHOICES = [
        ("Fresher", "Fresher"),
        ("Mid", "Mid Level"),
        ("Senior", "Senior"),
    ]
    
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    experience_level = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the job listing.
        """
        return self.title
