from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Company
from .serializers import CompanySerializer
from .permissions import IsRecruiter


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsRecruiter]


class CompanyDetailView(generics.RetrieveAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get_object(self):
        return self.request.user.company
