from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from .models.artist import Artist
from .serializer import ArtistSerializer

from .models.album import Album
from .serializer import AlbumSerializer

from .models.song import Song
from .serializer import SongSerializer

class ArtistApiView(views.APIView):

    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

class AlbumApiView(views.APIView):

    def get(self, request):
        album = Album.objects.all()
        serializer = AlbumSerializer(album, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =AlbumSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SongApiView(views.APIView):
    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)



