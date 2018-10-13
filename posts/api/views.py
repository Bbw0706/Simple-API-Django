from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from ..serializers import PostSerializer
from ..models import Posts

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
