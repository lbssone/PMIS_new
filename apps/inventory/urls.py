from django.urls import path

from .views import InventoryList, ScheduleForm, ProductUpdate, ComponentUpdate, MaterialUpdate

app_name = "inventory"

urlpatterns = [
    path('', InventoryList.as_view(), name='list'),
    # path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('schedule', ScheduleForm.as_view(), name='schedule_form'),
    path('product/<int:pk>/update', ProductUpdate.as_view(), name='product_update'),
    path('component/<int:pk>/update', ComponentUpdate.as_view(), name='component_update'),
    path('material/<int:pk>/update', MaterialUpdate.as_view(), name='material_update')
]
