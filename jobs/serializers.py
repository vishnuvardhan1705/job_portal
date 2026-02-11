from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'description',
            'location',
            'salary',
            'job_type',
            'company',
            'company_name',
            'created_at'
        )
        read_only_fields = ('company',)

    def create(self, validated_data):
        user = self.context['request'].user

        if not hasattr(user, 'company'):
            raise serializers.ValidationError(
                "Recruiter must create a company first."
            )

        return Job.objects.create(
            company=user.company,
            **validated_data
        )
