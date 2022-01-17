from rest_framework.viewsets import ModelViewSet
from .models import Ubicacion
from .serializers import UbicacionSerializer

class UbicacionViewSet(ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer