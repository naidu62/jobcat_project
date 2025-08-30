from django.db import models

class Job(models.Model):
    """
    A model to represent a job listing.
    """
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.CharField(max_length=100) # Using CharField to allow for ranges like "$50k - $60k"
    location = models.CharField(max_length=200, default='Remote')
    experience_level = models.CharField(max_length=100, default='Entry-level')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the job listing.
        """
        return self.title
