from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Paciente
from ..serializers import PacienteSerializer
from ..permissions.grupos import IsAdministrador

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
