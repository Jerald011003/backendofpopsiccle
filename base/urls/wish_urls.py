from django.urls import path
from base.views import song_views as views

urlpatterns = [
    path('', views.get_songs, name='get_songs'),
    path('top/', views.get_top_songs, name='get_top_songs'),
    path('<str:pk>/', views.get_song, name='get_song'),
    path('create/', views.create_song, name='create_song'),
    path('<str:pk>/update/', views.update_song, name='update_song'),
    path('<str:pk>/delete/', views.delete_song, name='delete_song'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('<str:pk>/reviews/', views.create_song_review, name='create_song_review'),
]
