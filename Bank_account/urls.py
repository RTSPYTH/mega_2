from rest_framework.routers import SimpleRouter

from .views import BankAccountAPIView

router = SimpleRouter()
router.register("", BankAccountAPIView, basename='BankAccount')

urlpatterns = []
urlpatterns += router.urls
