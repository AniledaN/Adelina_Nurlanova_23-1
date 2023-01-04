from django.db import models

# Create your models here.


class Stuff(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)
    rate = models.FloatField()


class Comment(models.Model):
    comms = models.ForeignKey(Stuff, on_delete=models.CASCADE, null=True, related_name="comments")
    text = models.TextField()
    created_date = models.DateField(auto_now=True)
