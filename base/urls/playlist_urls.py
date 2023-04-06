from django.urls import path
from base.views import playlist_views as views

urlpatterns = [
    path('create/', views.PlaylistCreateAPIView.as_view(), name='playlist-create'),
    path('list/', views.PlaylistListAPIView.as_view(), name='playlist-list'),
    path('<int:pk>/', views.PlaylistDetailAPIView.as_view(), name='playlist-detail'),
]
