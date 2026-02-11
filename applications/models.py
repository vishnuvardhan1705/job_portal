from django.db import models
from django.conf import settings
from jobs.models import Job

User = settings.AUTH_USER_MODEL


class Application(models.Model):
    STATUS_CHOICES = (('APPLIED', 'Applied'),('SHORTLISTED', 'Shortlisted'),('REJECTED', 'Rejected'),)

    job = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='applications')
    applicant = models.ForeignKey(User,on_delete=models.CASCADE,related_name='applications')
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='APPLIED')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'applicant')

    def __str__(self):
        return f"{self.applicant} → {self.job}"
