from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from base.models import Playlist
from base.serializers import PlaylistSerializer
from rest_framework import status



class PlaylistCreateAPIView(generics.CreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaylistListAPIView(generics.ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    # permission_classes = [permissions.AllowAny]

class PlaylistDetailAPIView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    # permission_classes = [permissions.AllowAny]
