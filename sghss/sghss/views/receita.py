from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Receita
from ..serializers import ReceitaSerializer
from ..permissions.grupos import IsAdministrador, IsProfissionalSaude, IsPaciente

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    permission_classes = [IsAuthenticated, IsProfissionalSaude | IsPaciente | IsAdministrador]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Receita.objects.all()

        if user.groups.filter(name='Paciente').exists():
            try:
                paciente = Paciente.objects.get(user=user)
                return Receita.objects.filter(consulta__paciente=paciente)
            except Paciente.DoesNotExist:
                return Receita.objects.none()

        elif user.groups.filter(name='ProfissionalSaude').exists():
            return Receita.objects.all()

        elif user.groups.filter(name='Administrador').exists():
            return Receita.objects.all()

        return Receita.objects.none()
