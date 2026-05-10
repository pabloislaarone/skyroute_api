from rest_framework.routers import DefaultRouter
from .views import AerolineaViewSet, VueloViewSet

router = DefaultRouter()
router.register(r'aerolineas', AerolineaViewSet)
router.register(r'vuelos', VueloViewSet)

urlpatterns = router.urls