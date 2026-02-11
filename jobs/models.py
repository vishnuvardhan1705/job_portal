from django.db import models
from django.db import models
from companies.models import Company


class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ('FULL_TIME', 'Full Time'),
        ('PART_TIME', 'Part Time'),
        ('INTERNSHIP', 'Internship'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
