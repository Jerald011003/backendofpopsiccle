# urls.py

from django.urls import path
from base.views import chatfriend_views as views

urlpatterns = [
    path('add_friend/', views.add_friend, name='add_friend'),
    path('get_friends/', views.get_friends, name='get_friends'),
    path('chat/', views.chat, name='chat'),
    path('get_chat/<int:friend_id>/', views.get_chat, name='get_chat')
]
