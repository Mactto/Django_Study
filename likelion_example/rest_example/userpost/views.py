from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
# Create your views here.

class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs

        return qs