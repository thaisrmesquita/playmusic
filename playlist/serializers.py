from rest_framework import serializers
from playlist.models import Record
from playlist.models import *

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ('url','name',)

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('url','name')

class BandSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(), slug_field='name')
    class Meta:
        model = Band
        fields=('url','name','genre','record')

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    band = serializers.SlugRelatedField(queryset=Band.objects.all(), slug_field='name')
    playlist = serializers.SlugRelatedField(queryset=Playlist.objects.all(), slug_field='name')
    class Meta:
        model = Music
        fields = ('url','name','band','duration','year','playlist')


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = ('url','name')


