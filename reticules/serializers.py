from rest_framework.serializers import ModelSerializer

from reticules.models import Reticule


class ReticuleSerializer(ModelSerializer):
    class Meta:
        model = Reticule
        fields = "__all__"
