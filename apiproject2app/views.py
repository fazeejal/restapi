from rest_framework import generics
from .models import Sample
from .serializers import SampleSerializer

class AllSampleList(generics.ListAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

class ActiveSampleList(generics.ListCreateAPIView):
    queryset = Sample.objects.filter(is_active=True)
    serializer_class = SampleSerializer 

class ActiveSampleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sample.objects.filter(is_active=True)
    serializer_class = SampleSerializer
