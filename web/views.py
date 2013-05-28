from rest_framework import viewsets
from rest_framework import permissions as rest_permissions

from web import models
from web import serializers
from web import permissions


class CompanyViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows companies to be viewed
    """
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = (
        rest_permissions.IsAuthenticatedOrReadOnly,
        permissions.IsOwnerOrReadOnly,
    )

    def pre_save(self, obj):
        obj.owner = self.request.user
