from rest_framework.routers import DefaultRouter
from .views import UbicacionViewSet
from django.urls import include, path


from django.contrib import admin

router = DefaultRouter()
router.register('api', UbicacionViewSet)

urlpatterns = [
    path('ubicacion/', include(router.urls))
]