from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drf.serializers import User_Serializers, Group_Serializers


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = User_Serializers


class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = Group_Serializers


