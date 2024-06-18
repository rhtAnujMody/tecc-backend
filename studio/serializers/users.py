from rest_framework import serializers
from studio.models import User
from studio.configs import Constants
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from django.core.validators import EmailValidator, RegexValidator

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'full_name', 'gender', 'phone_number', 'profile_photo', 'country', 'city', 'top_seller']


    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self,obj):
        return obj.last_name.title()

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'
    

    '''def to_representation(self, instance):
        representation = super(UserProfileSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["role"] = Constants.ADMIN
        return representation'''
        

class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields =  ["id", "email", "first_name", "last_name", "password"]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.is_active = True  # Automatically activate the user
        user.save()
        return user
