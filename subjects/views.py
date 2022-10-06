from rest_framework.viewsets import ModelViewSet

from subjects.models import Subject
from subjects.serializers import SubjectSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
