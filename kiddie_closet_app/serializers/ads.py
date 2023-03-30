import datetime

from rest_framework import serializers

from kiddie_closet_app.models import Ad


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"

    def create(self, validated_data):
        # Set the order_date automatically
        validated_data["published_date"] = datetime.datetime.now()
        new_ad = Ad.objects.create(**validated_data)
        return new_ad

