from rest_framework.serializers import ModelSerializer, ReadOnlyField

from subjects.models import Subject


class SubjectSerializer(ModelSerializer):
    total_hours = ReadOnlyField()

    class Meta:
        model = Subject
        fields = "__all__"
