from rest_framework import serializers
from django.contrib.auth import get_user_model

class ChangePass(serializers.Serializer):
    old_password= serializers.CharField(required=True)
    new_password= serializers.CharField(required=True)

class Register(serializers.ModelSerializer):
    username= serializers.CharField()
    email= serializers.EmailField()
    password= serializers.CharField(write_only=True,min_length=6)
    passwordRavno= serializers.CharField(write_only=True,min_length=6)
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'passwordRavno']
    def validate(self, data):
        if data['password']!=data['passwordRavno']:
            raise serializers.ValidationError('Уже забыл? Боже ты же ток что написал пароль!')
        return data
    def create(self, validated_data):
        validated_data.pop('passwordRavno')
        return get_user_model().objects.create_user(**validated_data)
        
