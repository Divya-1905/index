from django.shortcuts import render
from.models import consumer,products
from rest_framework.permissions import AllowAny
from rest_framework.generics  import CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_100_CONTINUE,HTTP_201_CREATED,HTTP_404_NOT_FOUND,HTTP_206_PARTIAL_CONTENT
from .serializer import consumerserializer,productsserializer


class consumercreate(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = consumerserializer
    def create(self, request, *args, **kwargs):
        serializer = consumerserializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'status':'consumer created'},status=HTTP_201_CREATED)
            except Exception as e:
                return Response({'stauts':'not crated','data':serializer.errors},status=HTTP_404_NOT_FOUND)    
class consumerEditView(RetrieveUpdateAPIView):
    permission_classes =[AllowAny]
    serializer_class = consumerserializer
    queryset = consumer.objects.all()
    def retrieve(self, request,pk):
       try:
        print('hai')
        queryset = consumer.objects.get(pk=pk)
       except:
        print('hai')
        return Response({'status':'consumer_not_deleted'},status=HTTP_404_NOT_FOUND)
    def update(self, request,pk):
        try:
            queryset = consumer.objects.get(pk=pk)
            print(queryset)
        except Exception as e:
            return Response({'status':'consumer_not_updated','data':e},status=HTTP_206_PARTIAL_CONTENT)   