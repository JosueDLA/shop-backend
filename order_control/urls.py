from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user-type', views.UserTypeViewSet, 'user-type')
router.register(r'user', views.UserViewSet, 'users')
router.register(r'product', views.ProductViewSet, 'products')
router.register(r'order-detail', views.OrderDetailViewSet, 'order-detail')
router.register(r'order', views.OrderViewSet, 'order')

urlpatterns = router.urls
