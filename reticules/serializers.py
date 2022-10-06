from rest_framework.serializers import ModelSerializer

from reticules.models import Reticule
from subjects.serializers import SubjectSerializer


class ReticuleSerializer(ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Reticule
        fields = "__all__"
