from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.author import AuthorList, AuthorDetail
from .views.genre import GenreViewSet
from .views.language import LanguageViewSet

router = DefaultRouter()
# router.register(r'books', BookViewset)
# router.register(r'bookinstances', BookInstanceViewset)
router.register(r'genres', GenreViewSet)
router.register(r'languages', LanguageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('authors/', AuthorList.as_view()),
    path('authors/<int:pk>/', AuthorDetail.as_view()),
]
