# views.py
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Friend, Chat
from django.contrib.auth.models import User

@csrf_exempt
@api_view(['POST'])
def add_friend(request):
    if request.method == 'POST':
        user = get_object_or_404(User, id=request.user.id)
        friend_name = request.POST.get('friend_name')
        friend = Friend.objects.create(user=user, name_of_friend=friend_name)
        return JsonResponse({'message': 'Friend added successfully!', 'friend_id': friend._id})
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_friends(request):
    friends = Friend.objects.filter(user=request.user)
    data = []
    for friend in friends:
        data.append({
            'friend_id': friend._id,
            'name_of_friend': friend.name_of_friend,
            'rating': friend.rating,
            'comment': friend.comment
        })
    return Response(data)

@csrf_exempt
@api_view(['POST'])
def chat(request):
    if request.method == 'POST':
        friend_id = request.POST.get('friend_id')
        friend = get_object_or_404(Friend, _id=friend_id)
        message = request.POST.get('message')
        chat = Chat.objects.create(user=request.user, friend=friend, message=message)
        return JsonResponse({'message': 'Message sent successfully!'})
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_chat(request, friend_id):
    friend = get_object_or_404(Friend, _id=friend_id)
    chats = Chat.objects.filter(user=request.user, friend=friend)
    data = []
    for chat in chats:
        data.append({
            'message': chat.message,
            'created_at': chat.created_at
        })
    return Response(data)
