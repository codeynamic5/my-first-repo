from django.db import models
from django.contrib.auth.models import User
import uuid

class MoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=255, default="")
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()

    @property
    def is_mood_strong(self): # mengukur mood berdasarkan mood_intensity
        return self.mood_intensity > 5