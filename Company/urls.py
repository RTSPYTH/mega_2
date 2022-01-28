from rest_framework.routers import SimpleRouter

from .views import CompanyAPIView

router = SimpleRouter()
router.register("", CompanyAPIView, basename='Company')

urlpatterns = []
urlpatterns += router.urls
