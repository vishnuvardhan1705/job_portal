from django.shortcuts import render
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Job
from .serializers import JobSerializer
from .permissions import IsRecruiter, IsJobOwner
from .filters import JobFilter


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = JobFilter

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsRecruiter()]
        return [permissions.AllowAny()]


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer
    permission_classes = [IsRecruiter, IsJobOwner]
