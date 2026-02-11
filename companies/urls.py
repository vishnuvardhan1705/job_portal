from django.urls import path
from .views import CompanyCreateView, CompanyDetailView

urlpatterns = [
    path('create/', CompanyCreateView.as_view()),
    path('me/', CompanyDetailView.as_view()),
]
