from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    #created_hour = models.TimeField()
    #published_hour = models.TimeField
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
