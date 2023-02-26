from .models import Run
#from django.contrib.auth.models import User, Group
from rest_framework import serializers

#Our RunSerializer
class RunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Run
        fields = ['id', 'subject', 'details']