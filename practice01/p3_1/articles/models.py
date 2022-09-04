from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    memo = models.CharField(max_length=20, default='')

    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.content} / {self.memo}'

class Movie(models.Model):
    title = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 15)
    director = models.CharField(max_length = 20, default='unknown')

    def __str__(self):
        return f'{self.title} {self.genre}'