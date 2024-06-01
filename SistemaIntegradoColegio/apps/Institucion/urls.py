from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import InstitucionViewSet, RedSocialViewSet, SedeViewSet

router = DefaultRouter()
router.register(r'instituciones', InstitucionViewSet)
router.register(r'redes-sociales', RedSocialViewSet)
router.register(r'sedes', SedeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
