from .models import User,signup,login
from rest_framework import serializers 
class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ="__all__"
class signupserializer(serializers.ModelSerializer):
    class Meta:
        model = signup
        fields =['name','password'] 
        def create(self,request,validated_data):
            data = signup.objects.create(name=validated_data['name'],password = validated_data['password'] )
            data.set_password(raw_password=validated_data['password']) 
            data.save()
            return data
        def validate(self,request,data):
            data = signup.objects.all()
            if self.instance:
                id = self.instance.id
                queryset = data.exclude(id=id)
                if queryset.filter(email=data['email']).exists():
                    raise serializers.ValidationError({'error':'email already exists'})
                elif queryset.filter(phone= data['phone']).exists():
                    raise serializers.ValidationError({'status':'phone aleady exists'})
                return data
        
        
        
        
        # def validate(self, data):
        #     queryset = User.objects.all()
        #     if self.instance:
        #         id = self.instance.id
        #     queryset = queryset.exclude(id=id)
        #     if queryset.filter(email=data['email']).exists():
        #         raise serializers.ValidationError(
        #         {'error': 'email already exists'})
        #     elif queryset.filter(phone=data['phone']).exists():
        #         raise serializers.ValidationError(
        #         {'error': 'phone already exists'})
        #     return data

        # def validate(self,request):
        #     data = User.objects.all()
        #     if self.instance:
        #         id = self.instance.id
        #         data = data.exclude(id=id)
                
                
                
                
                
                
                   
                         
class logserializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'        