from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user-type', views.UserTypeViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'order-detail', views.OrderDetailViewSet)
router.register(r'order', views.OrderViewSet)

urlpatterns = router.urls
