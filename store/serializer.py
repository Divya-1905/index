from.models import Grocery,Clothing,Stateonery,Electronic,Furiniture,consumer
from rest_framework import serializers


class consumerserializer(serializers.ModelSerializer):
    class Meta:
        model = consumer
        fields = '__all__'
# class productsserializer(serializers.ModelSerializer):
#     class Meta:
#         model = products
#         fields = '__all__'    
class Groceryserializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = '__all__'
class Clothingseriallizer(serializers.ModelSerializer): 
    class Meta:
        model = Clothing
        fields = '__all__'
class statoneryserializer(serializers.ModelSerializer):
    class Meta:
        model = Stateonery
        fields = '__all__' 
class Electronicserializer(serializers.ModelSerializer):
    class Meta:
        model = Electronic
        fields = '__all__'     
class Furinitureseriliazer(serializers.ModelSerializer):
    class Meta:
        model = Furiniture
        fields = '__all__'                            