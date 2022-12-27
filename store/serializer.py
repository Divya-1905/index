from.models import consumer,products
from rest_framework import serializers


class consumerserializer(serializers.ModelSerializer):
    class Meta:
        model = consumer
        fields = '__all__'
class productsserializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'        