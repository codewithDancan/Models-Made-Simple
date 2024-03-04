from django.db import models


class PostMusic(models.Model):
    artist_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    mp3_file = models.FileField(upload_to='mp3_files/', blank=True)
    song_cover = models.ImageField(upload_to='images/')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title