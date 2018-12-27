from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView
import apps.inventory.urls as inventory_routes
import apps.member.urls as member_routes

urlpatterns = [
    path('', TemplateView.as_view(template_name='modules/index/index.html'), name='homepage'),
    path('inventory/', include(inventory_routes)),
    path('member/', include(member_routes)),
    path('admin/', admin.site.urls),
]
