from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, filters, permissions, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)

from .filters import TitleFilter
from .models import Category, Comment, Genre, Review, Title
from .permissions import IsAdministratorOrReadOnly, IsStaffOrOwnerOrReadOnly
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleCreateSerializer, TitleListSerializer)


class BaseCreateListDestroyViewSet(
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoriesViewSet(BaseCreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAdministratorOrReadOnly, ]
    search_fields = ['=name', ]
    lookup_field = 'slug'


class GenresViewSet(BaseCreateListDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAdministratorOrReadOnly, ]
    search_fields = ['=name', ]
    lookup_field = 'slug'


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter
    permission_classes = [IsAdministratorOrReadOnly, ]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TitleCreateSerializer
        return TitleListSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsStaffOrOwnerOrReadOnly]

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()
        # queryset = self.queryset
        # return queryset.filter(title_id=self.kwargs['title_id'])

    def perform_create(self, serializer):
        get_object_or_404(Title, id=self.kwargs.get('title_id')) 
        serializer.save(author=self.request.user) 
        # title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        # serializer.save(author=self.request.user, title=title)
        # title.update_rating()

    # def perform_update(self, serializer):
    #     title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
    #     serializer.save(author=self.request.user, title_id=title)
    #     title.update_rating()

    # def perform_destroy(self, instance):
    #     title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
    #     instance.delete()
    #     title.update_rating()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsStaffOrOwnerOrReadOnly]

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments.all()
        # queryset = self.queryset
        # return queryset.filter(review_id=self.kwargs['review_id'])

    def perform_create(self, serializer):
        get_object_or_404(Review, id=self.kwargs.get('review_id')) 
        serializer.save(author=self.request.user)
        # review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        # serializer.save(author=self.request.user, review_id=review)
