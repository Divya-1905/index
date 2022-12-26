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
# class logserializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['last_login']






    # def create(self,validated_data):
    #     data = User.object.c(email = validated_data['email'],
    #     password = validated_data['password'],address= validated_data['address'],
    #     name = validated_data['name'],phone=validated_data['phone'])
    #     data.save()
    #     return data 


