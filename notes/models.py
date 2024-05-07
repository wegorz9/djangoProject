from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    PRIORITY_CHOICES = [
        (0, "Max"),
        (1, "Important"),
        (2, "Standard"),
        (3, "Unimportant"),
    ]

    title = models.CharField(max_length=255)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title