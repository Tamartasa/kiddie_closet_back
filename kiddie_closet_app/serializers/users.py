from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from kiddie_closet_app.models import AppUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=User.objects.all())])
    # password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'is_staff', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate_is_staff(self, value):
        if value and not self.context['request'].user.is_staff:
            raise serializers.ValidationError("You do not have permission to set is_staff to True.")
        return value


    def validate(self, attrs):
        if 'is_staff' in attrs and attrs['is_staff'] and not self.context['request'].user.is_staff:
            raise serializers.ValidationError("You do not have permission to create staff users.")

        return attrs

    def create(self, validated_data):
        is_staff = validated_data.pop('is_staff', False)
        if is_staff and not self.context['request'].user.is_staff:
            raise serializers.ValidationError("You do not have permission to create staff users.")
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=is_staff
        )
        user.set_password(validated_data['password'])
        user.save()

        appuser= AppUser.objects.create(
            id=user,
            city=validated_data['city'],
            neighborhood=validated_data['neighborhood']
        )
        appuser.save()


        return user