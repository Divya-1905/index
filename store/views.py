from django.shortcuts import render
from.models import Furiniture,Clothing,Stationery,Grocery,Consumer
from rest_framework.permissions import AllowAny
from rest_framework.generics  import (CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,ListCreateAPIView)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_100_CONTINUE,
HTTP_201_CREATED,HTTP_404_NOT_FOUND,
HTTP_200_OK,HTTP_206_PARTIAL_CONTENT)
from .serializer import (stationeryserializer,
Clothingseriallizer,Furinitureseriliazer,
consumerserializer,Groceryserializer)


class consumer_create(ListCreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = consumerserializer
    print(serializer_class)

    queryset = Consumer.objects.all()  
    def list(self,request):
       queryset = Consumer.objects.all() 
       print(consumerserializer)
       serializer = consumerserializer(queryset, many=True)

       return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = consumerserializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'status':'consumer created'},status=HTTP_201_CREATED)
            except Exception as e:
                return Response({'stauts':'not crated','data':serializer.errors},status=HTTP_404_NOT_FOUND)  
    


class consumerEditView(RetrieveUpdateDestroyAPIView):
    permission_classes =[AllowAny]
    serializer_class = consumerserializer
    queryset = Consumer.objects.all()
    
    def retrieve(self,request,pk):
        try:
             
             queryset = Consumer.objects.get(id=pk)
             print(queryset)
             serializer = consumerserializer(queryset)
             return Response(serializer.data,status=HTTP_200_OK)
        except:
            print('hello')
            return Response({"status":"consumer_not_exitst"},status=HTTP_206_PARTIAL_CONTENT)

class GroceryView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = Groceryserializer
    def list(self,request):
        queryset = Grocery.objects.all()
        serializer = Groceryserializer(queryset, many=True)
        return Response(serializer.data)
    def post(self,request):
        seriliazer = Groceryserializer(data=request.data)
        if seriliazer.is_valid():
            try:
                seriliazer.save()
                return Response({'status':'Grocery created'},status= HTTP_200_OK)
            except Exception as e:     
                return Response({'status':'grocerynot crated','data':seriliazer.errors},status=HTTP_206_PARTIAL_CONTENT)
class GroceryEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class  = Groceryserializer
    queryset = Grocery.objects.all()
    def retrive(self,request,pk):
        try:
            queryset = Grocery.objects.get(id=pk)
            serializer = Groceryserializer(queryset)
            return Response(serializer.data,status=HTTP_200_OK)
        except:
            return Response({"status":"Gerocery_Id_doesnot_exist"},status=HTTP_206_PARTIAL_CONTENT)

class StationeryCreate(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = stationeryserializer
    def list(self,request):
        queryset = Stationery.objects.all()
        serializer = stationeryserializer(queryset, many= True)
        return Response(serializer.data)
    def post(self,request):
        serializer = stationeryserializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'status':'statonery created'},status= HTTP_200_OK)
            except:
                return Response({'status':'statonery is not crated'},status=HTTP_206_PARTIAL_CONTENT)
class StationeryEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = stationeryserializer
    queryset = Stationery.objects.all()
    def retrive(self,request,pk):
        try:
            queryset = Stationery.objects.get(id=pk)
            serializer = stationeryserializer(queryset)
            return Response(serializer.data,status=HTTP_100_CONTINUE)
        except:
            return Response({'status':'statonery is not updated'},status=HTTP_206_PARTIAL_CONTENT)    

class ClothingCreate(APIView):
    permission_classes = [AllowAny]
    serializer_class = Clothingseriallizer
    def post(self,request):
        queryset = Clothing.objects.all()
        serializer = Clothingseriallizer(data=request.data)
        return Response(serializer.data)
    def post(self,request):
        serializer = Clothingseriallizer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'status':'clothing created'},status=HTTP_200_OK)
            except:
                return Response({'status':'clothing is not created'},status=HTTP_206_PARTIAL_CONTENT) 
                       
class ClothingEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = Clothingseriallizer
    queryset = Clothing.objects.all()
    def retrive(self,request,pk):
        data = Clothingseriallizer.get(id=pk)
        try:
            serializer = Clothingseriallizer(data=data)
            return Response(serializer.data,status=HTTP_100_CONTINUE)
        except:
            return Response({'status':'clothing is not updated'},status=HTTP_206_PARTIAL_CONTENT)    
class Funriniturecreate(APIView):
    permission_classes = [AllowAny]
    serializer_class = Furinitureseriliazer
    def list(self,requsest):
        queryset = Furinitureseriliazer.objects.all()
        serializer = Furinitureseriliazer(queryset)
        return Response(serializer.data)
    def post(self,request):
        serializer = Furinitureseriliazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'funriniture created'},status=HTTP_200_OK)
        return Response({'status':'funriniture is not created','data':serializer.errors},status= HTTP_206_PARTIAL_CONTENT) 
class FunrinitureEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny] 
    serializer_class = Furinitureseriliazer
    queryset = Furiniture.objects.all()
    def retrive(self,request,pk):
       queryset = Furiniture.objects(id=pk)
       try:
          serializer = Furinitureseriliazer(queryset = queryset)
          return Response(serializer.data,status=HTTP_200_OK)
       except:
        return Response({'status':'Funriniture id  is not updated'},status=HTTP_206_PARTIAL_CONTENT)    
class consumerprofileEdit(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = consumerserializer
    queryset = Consumer.objects.all()
    def retieve(self,request,pk):
        try:
            queryset = Consumer.objects(id=pk)
            serializer = consumerserializer(queryset = queryset)
            return Response(serializer.data,status=HTTP_200_OK)
        except:
            return Response({'status':'consumerprofile_id_doesnot exist '},status=HTTP_206_PARTIAL_CONTENT)    