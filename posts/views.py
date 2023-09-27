from django.db.models import Count
from rest_framework import generics, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer, TagSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from taggit.models import Tag



class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
        # tags_count=Count('tags', distinct=True),
    ).order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at',
        # 'tags_count',
    ]

    search_fields = [
        'owner__username',
        'title',
        'tags__name'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class TagListView(generics.ListAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')
    serializer_class = PostSerializer

@api_view(['POST'])
def create_tag(request):
    tag_name = request.data.get('tag')
    if tag_name:
        tag, created = Tag.objects.get_or_create(name=tag_name)
        if created:
            return Response({'message': f'Tag "{tag_name}" created successfully.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': f'Tag "{tag_name}" already exists.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Tag name is required.'}, status=status.HTTP_400_BAD_REQUEST)


class TagListView(generics.ListAPIView):
#     def get(self, request, format=None):
        # Fetch all tags
    queryset = Tag.objects.all()

         # Serialize the tags
    serializer_class = TagSerializer

#         return Response(serializer_class.data)
