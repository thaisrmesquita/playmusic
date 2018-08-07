from django.db import models
from django.db.models import CASCADE


class Record(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name' , )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=CASCADE, related_name="bands")
    record = models.ForeignKey(Record, related_name='records_bands', on_delete=CASCADE)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=100)
    band = models.ForeignKey(Band,related_name="band_musics", on_delete=CASCADE)
    duration = models.TimeField()
    year = models.DateField()
    playlist = models.ForeignKey(Playlist, related_name="musics", on_delete=CASCADE)


    def __str__(self):
        return self.name

