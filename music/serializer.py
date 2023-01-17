from rest_framework import serializers
from .models import album, artist, song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = artist.Artist

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = album.Album

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = song.Song



