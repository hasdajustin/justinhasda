from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_project_url(self):
        return self.live_link if self.live_link else self.github_link

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class HireRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project_type = models.CharField(max_length=200)
    budget = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.project_type}"
