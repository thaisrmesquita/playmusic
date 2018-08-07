from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from playlist.models import *
from playlist.serializers import *
from rest_framework.response import Response
from rest_framework.reverse import reverse

class RecordList(generics.ListCreateAPIView):
	queryset = Record.objects.all()
	serializer_class = RecordSerializer
	name = 'record-list'

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Record.objects.all()
	serializer_class = RecordSerializer
	name = 'record-detail'

class GenreList(generics.ListCreateAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
	name = 'genre-list'

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
	name = 'genre-detail'

class BandList(generics.ListCreateAPIView):
	queryset = Band.objects.all()
	serializer_class = BandSerializer
	name = 'band-list'

class BandDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Band.objects.all()
	serializer_class = BandSerializer
	name = 'band-detail'

class MusicList(generics.ListCreateAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer
	name = 'music-list'

class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer
	name = 'music-detail'

class PlaylistList(generics.ListCreateAPIView):
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer
	name = 'playlist-list'

class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Playlist.objects.all()
	serializer_class = PlaylistSerializer
	name = 'playlist-detail'''

class ApiRoot(generics.GenericAPIView):
	name = 'api-root'
	def get(self, request, *args, **kwargs):
		return Response({
			'records':reverse(RecordList.name, request=request),
			'genres': reverse(GenreList.name, request=request),
			'bands': reverse(BandList.name, request=request),
			'musics': reverse(MusicList.name, request=request),
			'playlists': reverse(PlaylistList.name, request=request)
		})
