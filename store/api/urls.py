from django.urls import include, path
from rest_framework import routers

from views import BasketModelViewSet, ProductModelViewSet, UserListAPIView

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet)
router.register(r'baskets', BasketModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user-list/', UserListAPIView.as_view(), name='user_list'),
]
