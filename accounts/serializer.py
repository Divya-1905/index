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
class logserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['phone','address','last_login','name']
     

