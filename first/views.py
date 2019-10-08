from rest_framework import viewsets
from first.models import Author
from first.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
