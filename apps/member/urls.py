from django.urls import path

from .views import MemberList

app_name = "member"

urlpatterns = [
    path('', MemberList.as_view(), name='list'),
    # path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]
