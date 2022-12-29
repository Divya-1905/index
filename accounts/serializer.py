from .models import User
from rest_framework import serializers 



class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name,phone']
class signupserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['last_login']
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user 
class logserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['phone','address','last_login','name']
     

