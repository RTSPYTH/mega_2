from rest_framework.routers import SimpleRouter

from .views import LeaderAPIView

router = SimpleRouter()
router.register("", LeaderAPIView, basename='Leader')

urlpatterns = []
urlpatterns += router.urls
