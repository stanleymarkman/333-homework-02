from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)

class ArtistAttributes(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    genre = models.CharField(max_length=255)
    birth_location = models.CharField(max_length=255)
    birth_year = models.IntegerField(default=2000)

    def __str__(self):
        return self.name + '' + self.genre + '' + self.birth_location + '' + self.birth_year

class Artists(models.Model):
    song = models.CharField(max_length=255, primary_key=True)
    artist = models.ForeignKey(ArtistAttributes, on_delete=models.RESTRICT)

class Ratings(models.Model):
    username = models.ForeignKey(Users, on_delete=models.RESTRICT)
    song = models.ForeignKey(Artists, on_delete=models.RESTRICT)
    rating = models.IntegerField(default=1)
    
    class Meta:
        models.UniqueConstraint(fields=['username', 'song'], name='user_song_composite')