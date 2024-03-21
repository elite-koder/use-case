from rest_framework.routers import DefaultRouter
from feature_toggle.views import FeatureToggleViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('v1/feature_toggles', FeatureToggleViewSet, basename='feature-toggles')
urlpatterns = [path('', include(router.urls))]