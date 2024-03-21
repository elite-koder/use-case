from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from feature_toggle.serializers import FeatureToggleSerializer
from feature_toggle.models import FeatureToggle
from rest_framework.decorators import action


class FeatureToggleViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = FeatureToggleSerializer
    queryset = FeatureToggle.objects.all()
    
    @action(detail=True, methods=['patch'])
    def toggle_state(self, request, pk):
        instance = self.get_object()
        instance.toggle_state()
        return Response(data=self.get_serializer(instance).data)