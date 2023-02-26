from django.shortcuts import render
from .models import Run
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RunSerializer

class RunViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    permission_classes = [permissions.AllowAny]
