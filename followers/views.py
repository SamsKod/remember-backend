from rest_framework import generics, permissions
from .models import Follower
from .serializers import FollowerSerializer
from drf_api.permissions import IsOwnerOrReadOnly



class FollowList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)


class FollowDetail(generics.RetrieveDestroyAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()