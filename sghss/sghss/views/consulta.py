from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Consulta
from ..serializers import ConsultaSerializer
from ..permissions.grupos import IsAdministrador, IsProfissionalSaude, IsPaciente

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated, IsAdministrador | IsProfissionalSaude | IsPaciente]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Consulta.objects.all()

        if user.groups.filter(name='Paciente').exists():
            try:
                paciente = Paciente.objects.get(user=user)
                return Consulta.objects.filter(paciente=paciente)
            except Paciente.DoesNotExist:
                return Consulta.objects.none()

        elif user.groups.filter(name='ProfissionalSaude').exists():
            return Consulta.objects.all()

        elif user.groups.filter(name='Administrador').exists():
            return Consulta.objects.all()

        return Consulta.objects.none()
