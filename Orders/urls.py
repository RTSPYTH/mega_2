from rest_framework.routers import SimpleRouter

from .views import OrderAPIView

router = SimpleRouter()
router.register("", OrderAPIView, basename='Order')

urlpatterns = []
urlpatterns += router.urls





