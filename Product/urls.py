from rest_framework.routers import SimpleRouter

from .views import ProductAPIView

router = SimpleRouter()
router.register("", ProductAPIView, basename='Product')

urlpatterns = []
urlpatterns += router.urls
