from django.urls import path
from .views import (
    ApplyJobView,
    MyApplicationsView,
    RecruiterApplicationsView,
    ApplicationStatusUpdateView
)

urlpatterns = [
    path('apply/', ApplyJobView.as_view()),
    path('my/', MyApplicationsView.as_view()),
    path('recruiter/', RecruiterApplicationsView.as_view()),
    path('<int:pk>/status/', ApplicationStatusUpdateView.as_view()),
]
