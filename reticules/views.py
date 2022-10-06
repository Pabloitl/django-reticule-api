from rest_framework.viewsets import ModelViewSet

from reticules.models import Reticule
from reticules.serializers import ReticuleSerializer


class ReticuleModelViewSet(ModelViewSet):
    queryset = Reticule.objects.all()
    serializer_class = ReticuleSerializer
