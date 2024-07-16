from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password',
                  'first_name', 'last_name', 'age', 'phone']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            age=validated_data.get('age', ''),
            phone=validated_data.get('phone', '')
        )
        return user

    def update(self, instance, validated_data):
        # Actualiza los campos que se pueden cambiar
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.age = validated_data.get('age', instance.age)
        instance.phone = validated_data.get('phone', instance.phone)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
