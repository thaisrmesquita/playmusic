"""playmusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from playlist import views

urlpatterns = [
    path('records/', views.RecordList.as_view(), name=views.RecordList.name),
    path('records/<int:pk>/', views.RecordDetail.as_view(), name=views.RecordDetail.name),
    path('genres/', views.GenreList.as_view(), name=views.GenreList.name),
    path('genres/<int:pk>/', views.GenreDetail.as_view(), name=views.GenreDetail.name),
    path('bands/', views.BandList.as_view(), name=views.BandList.name),
    path('bands/<int:pk>/', views.BandDetail.as_view(), name=views.BandDetail.name),
    path('music/', views.MusicList.as_view(), name=views.MusicList.name),
    path('music/<int:pk>/', views.MusicDetail.as_view(), name=views.MusicDetail.name),
    path('playlists/', views.PlaylistList.as_view(), name=views.PlaylistList.name),
    path('playlist/<int:pk>/', views.PlaylistDetail.as_view(), name=views.PlaylistDetail.name),
    path('', views.ApiRoot.as_view(),name=views.ApiRoot.name)
]
