from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import PacienteViewSet, ConsultaViewSet, ReceitaViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'receitas', ReceitaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
