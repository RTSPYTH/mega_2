from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/Adress/', include('Adress.urls')),
    path('api/v1/Bank_account/', include('Bank_account.urls')),
    path('api/v1/Company/', include('Company.urls')),
    path('api/v1/Leader/', include('Leader.urls')),
    path('api/v1/Order/', include('Orders.urls')),
    path('api/v1/Product/', include('Product.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
