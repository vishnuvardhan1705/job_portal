from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Application
from .serializers import (
    ApplicationCreateSerializer,
    ApplicationListSerializer,
    ApplicationStatusUpdateSerializer
)
from .permissions import IsJobSeeker, IsRecruiterOwner


class ApplyJobView(generics.CreateAPIView):
    serializer_class = ApplicationCreateSerializer
    permission_classes = [IsAuthenticated, IsJobSeeker]


class MyApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)


class RecruiterApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(
            job__company__owner=self.request.user
        )


class ApplicationStatusUpdateView(generics.UpdateAPIView):
    serializer_class = ApplicationStatusUpdateSerializer
    permission_classes = [IsAuthenticated, IsRecruiterOwner]
    queryset = Application.objects.all()
