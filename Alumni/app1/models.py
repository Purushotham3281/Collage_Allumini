from django.db import models

# Create your models here.
class Alumi(models.Model):
    person=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    branch=models.CharField(max_length=100)
    passedout=models.IntegerField()
    achievements=models.TextField(max_length=2000)
    company=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    exp=models.IntegerField()
    workplace=models.CharField(max_length=200)
    github=models.URLField()
    linkedin=models.URLField()
    portfolio=models.URLField()
    image=models.ImageField(upload_to="media")


    def __str__(self):
        return self.branch
