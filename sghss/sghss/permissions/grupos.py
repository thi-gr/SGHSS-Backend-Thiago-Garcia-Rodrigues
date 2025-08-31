from rest_framework.permissions import BasePermission

class IsPaciente(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.groups.filter(name='Paciente').exists()

class IsProfissionalSaude(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.groups.filter(name='ProfissionalSaude').exists()

class IsAdministrador(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.groups.filter(name='Administrador').exists()
