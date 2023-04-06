# urls.py
from django.urls import path
# from .views import friend_list, add_friend
from base.views import friend_views as views
urlpatterns = [
    path('friends/', views.friend_list, name='friend-list'),
    path('friends/add/', views.add_friend, name='add-friend'),
]
