from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password',
                  'first_name', 'last_name', 'age', 'phone', 'occupation', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
        }

    def validate(self, data):
        if not self.instance and 'password' not in data:
            raise serializers.ValidationError(
                {'password': 'This field may not be blank.'})
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
