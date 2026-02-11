from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'website', 'created_at')

    def create(self, validated_data):
        user = self.context['request'].user

        if hasattr(user, 'company'):
            raise serializers.ValidationError(
                "You already have a company."
            )

        return Company.objects.create(owner=user, **validated_data)
