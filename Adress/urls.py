from rest_framework.routers import SimpleRouter

from .views import AdressAPIView

router = SimpleRouter()
router.register("", AdressAPIView, basename='Adress')

urlpatterns = []
urlpatterns += router.urls
