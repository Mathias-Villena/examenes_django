from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuoteViewSet, SongViewSet

router = DefaultRouter()
router.register(r'quotes', QuoteViewSet)
router.register(r'songs', SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
]