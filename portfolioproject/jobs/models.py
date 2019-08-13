from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200, default='')
    project_description = models.TextField(max_length=1000, default='')
    responsibilities = models.TextField(max_length=1000, default='')
    technologies = models.TextField(max_length=1000, default='')

    class Meta:
        ordering = ('-title', 'project_description')

    def __str__(self):
        return self.title