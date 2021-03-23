from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """ Topic which user is learn """
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """ Returns string representation of the model"""
        return self.text

class Entry(models.Model):
    """ information that has been learned by the user on whe topic """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """ Returns string representation of the model"""
        if len(self.text) <50:
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."
