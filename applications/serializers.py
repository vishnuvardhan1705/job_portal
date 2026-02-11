from rest_framework import serializers
from .models import Application


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'job')

    def validate(self, data):
        user = self.context['request'].user

        if user.role != 'JOB_SEEKER':
            raise serializers.ValidationError(
                "Only job seekers can apply for jobs."
            )

        if Application.objects.filter(
            job=data['job'],
            applicant=user
        ).exists():
            raise serializers.ValidationError(
                "You have already applied for this job."
            )

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        return Application.objects.create(
            applicant=user,
            **validated_data
        )


class ApplicationListSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)
    company_name = serializers.CharField(source='job.company.name', read_only=True)

    class Meta:
        model = Application
        fields = (
            'id',
            'job_title',
            'company_name',
            'status',
            'applied_at'
        )


class ApplicationStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('status',)
