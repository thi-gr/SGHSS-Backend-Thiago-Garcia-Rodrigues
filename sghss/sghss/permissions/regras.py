from rest_framework.permissions import BasePermission

class IsConsultaOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.paciente.user == request.user

class IsReceitaOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.consulta.paciente.user == request.user
