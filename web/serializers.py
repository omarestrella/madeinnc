from rest_framework import serializers

from web import models


class UserListingField(serializers.RelatedField):
    def to_native(self, user):
        return user.username


class CompanySerializer(serializers.ModelSerializer):
    owner = UserListingField()

    class Meta:
        model = models.Company
        fields = ('owner', 'name', 'url', 'description', 'authorized',)
