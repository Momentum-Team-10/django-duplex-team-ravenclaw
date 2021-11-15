from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey


# Create your models here.
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username




class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()
    deck = models.ForeignKey(
        'Deck', on_delete=models.CASCADE, default=None,)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.pk

    def __repr__(self):
        return f"<Card name={self.pk}>"




class Deck(models.Model):
    owner = models.ForeignKey(
        'User', on_delete=models.CASCADE, default=None,)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Deck name={self.title}>"

    
