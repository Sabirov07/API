
from django.contrib import admin
from django.urls import path
from music.views import ArtistApiView
from music.views import AlbumApiView
from music.views import SongApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', ArtistApiView.as_view()),
    path('album/', AlbumApiView.as_view()),
    path('song/', SongApiView.as_view()),
]
