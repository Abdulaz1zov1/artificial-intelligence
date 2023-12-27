from chipta.views import (YonalishViewSet, 
                    BekatViewSet, PoyezdViewSet,
                    ChiptaViewSet)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'yonalish', YonalishViewSet, basename='yonalish')
router.register(r'bekat', BekatViewSet, basename='bekat')
router.register(r'poyezd', PoyezdViewSet, basename='poyezd')
router.register(r'chipta', ChiptaViewSet, basename='chipta')

urlpatterns = router.urls