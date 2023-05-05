from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_date = models.DateField()
    blog_description = models.CharField(max_length=250)

    def __str__(self):
        return self.blog_title