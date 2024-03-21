from rest_framework.serializers import ModelSerializer
from feature_toggle.models import FeatureToggle

class FeatureToggleSerializer(ModelSerializer):
    class Meta:
        model = FeatureToggle
        exclude = ['note', 'env', 'app']