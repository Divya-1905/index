from.models import Clothing,Stationery,Electronic,Furiniture,Grocery,Consumer
from rest_framework import serializers


class consumerserializer(serializers.ModelSerializer):
    # measurements = serializers.SerializerMethodField("get_measuremenstchoice")
    class Meta:
        model =Consumer
        fields = '__all__' 
    # def get_measuremenstchoice(self,obj):
    #     print('hey')
    #     if self.get_attribute(Consumer.Products_choice) == ['grocery']:
    #         print('hai')
    #         return ('grams','grams'),('kilograms','kilograms') 

class Groceryserializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = '__all__'
   
class Clothingseriallizer(serializers.ModelSerializer): 
    class Meta:
        model = Clothing
        fields = '__all__'
class stationeryserializer(serializers.ModelSerializer):
    class Meta:
        model = Stationery
        fields = '__all__' 
class Electronicserializer(serializers.ModelSerializer):
    class Meta:
        model = Electronic
        fields = '__all__'     
class Furinitureseriliazer(serializers.ModelSerializer):
    class Meta:
        model = Furiniture
        fields = '__all__'                            
class Consumerprofileserializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = '__all__'        


       