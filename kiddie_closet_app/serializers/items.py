import datetime

from rest_framework import serializers

from kiddie_closet_app.models import Item, AppUser


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    def create(self, validated_data):
        # Set the default values for city and neighborhood based on the user's AppUser model
        # user = self.context['request'].user
        # app_user = AppUser.objects.get(user=user)
        # validated_data['city'] = app_user.city
        # validated_data['neighborhood'] = app_user.neighborhood

        # Set the order_date and total_price fields automatically
        validated_data["published_date"] = datetime.datetime.now()

        new_item = Item.objects.create(**validated_data)
        return new_item

