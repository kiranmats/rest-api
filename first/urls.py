from django.urls import path
from first.views import AuthorViewSet

urlpatterns = [
    path('authors/', AuthorViewSet.as_view({
        'get': 'list'}
    ), name='author-view')
]
