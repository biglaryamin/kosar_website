from django.db import models


class Article(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.TextField()
    # Image=models.ImageField()

    def __str__(self):
        return self.Title