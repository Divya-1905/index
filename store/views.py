from django.shortcuts import render
from.models import Furiniture,Clothing,Stateonery,Grocery,consumer
from rest_framework.permissions import AllowAny
from rest_framework.generics  import CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_100_CONTINUE,HTTP_201_CREATED,HTTP_404_NOT_FOUND,HTTP_200_OK,HTTP_206_PARTIAL_CONTENT
from .serializer import Groceryserializer,statoneryserializer,Clothingseriallizer,Furinitureseriliazer,consumerserializer


class consumer_create(CreateAPIView):
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
class consumerEditView(RetrieveUpdateDestroyAPIView):
    permission_classes =[AllowAny]
    serializer_class = consumerserializer
    queryset = consumer.objects.all()
    def retrieve(self,request,pk):
        try:
             queryset = consumer.objects.get(id=pk)
             print(queryset)
             serializer = consumerserializer(queryset)
             return Response(serializer.data,status=HTTP_200_OK)
        except:
            print('hello')
            return Response({"status":"consumer_not_exitst"},status=HTTP_206_PARTIAL_CONTENT)

class GroceryView(APIView):
    permission_classes = [AllowAny]
    serializer_class = Groceryserializer
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
    serializer__class  = Groceryserializer
    queryset = Grocery.objects.all()
    def retrive(self,request,pk):
        try:
            queryset = Grocery.objects.get(id=pk)
            serializer = Groceryserializer(queryset)
            return Response(serializer.data,status=HTTP_200_OK)
        except:
            return Response({"status":"Gerocery_Id_doesnot_exist"},status=HTTP_206_PARTIAL_CONTENT)

class StatenoeryCreate(APIView):
    permission_classes = [AllowAny]
    serializer_class = statoneryserializer
    def create(self,request):
        serializer = statoneryserializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({'status':'statonery created'},status= HTTP_200_OK)
            except:
                return Response({'status':'statonery is not crated'},status=HTTP_206_PARTIAL_CONTENT)
class StatenoeyEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = statoneryserializer
    def retrive(self,request,pk):
        try:
            queryset = Stateonery.objects.get(id=pk)
            serializer = statoneryserializer(queryset)
            return Response(serializer.data,status=HTTP_100_CONTINUE)
        except:
            return Response({'status':'statonery is not updated'},status=HTTP_206_PARTIAL_CONTENT)    

class ClothingCreate(APIView):
    permission_classes = [AllowAny]
    serializer_class = Clothingseriallizer
    def create(self,request):
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
    def retrive(self,request,pk):
        data = Clothingseriallizer.get(id=pk)
        try:
            serializer = Clothingseriallizer(data=data)
            return Response(serializer.data,status=HTTP_100_CONTINUE)
        except:
            return Response({'status':'clothing is not updated'},status=HTTP_206_PARTIAL_CONTENT)    
class Funriniture(APIView):
    permission_classes = [AllowAny]
    serializer_class = Furinitureseriliazer
    def create(self,request):
        serializer = Furinitureseriliazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'funriniture created'},status=HTTP_200_OK)
        return Response({'status':'funriniture is not created','data':serializer.errors},status= HTTP_206_PARTIAL_CONTENT) 
class FunrinitureEditView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny] 
    serializer_class = Furinitureseriliazer
    
    def retrive(self,request,pk) :
       queryset = Furiniture.objects(id=pk)
       try:
          serializer = Furinitureseriliazer(queryset = queryset)
          return Response(serializer.data,status=HTTP_100_CONTINUE)
       except:
        return Response({'status':'Funriniture id  is not updated'},status=HTTP_206_PARTIAL_CONTENT)    