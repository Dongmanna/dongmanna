# chat/models.py
from django.db import models
from django.utils import timezone
from main.models import Post

class Room(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    number = models.IntegerField()

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    user = models.CharField(max_length=1000000)