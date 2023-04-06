# views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from base.models import Friend
from base.serializers import FriendSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def friend_list(request):
    friends = Friend.objects.filter(user=request.user)
    serializer = FriendSerializer(friends, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_friend(request):
    friend = Friend(user=request.user, friend_id=request.data['friend_id'])
    friend.save()
    serializer = FriendSerializer(friend)
    return Response(serializer.data)
