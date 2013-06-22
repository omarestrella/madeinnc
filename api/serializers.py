from rest_framework import serializers

from api import models


class UserListingField(serializers.RelatedField):
    def to_native(self, user):
        return user.username


class CompanySerializer(serializers.ModelSerializer):
    owner = UserListingField()

    class Meta:
        model = models.Company
        fields = ('id', 'owner', 'name', 'url', 'description', 'authorized',)
