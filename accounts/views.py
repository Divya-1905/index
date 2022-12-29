from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import User
from .serializer import signupserializer,logserializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.status import(
    HTTP_100_CONTINUE,HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_206_PARTIAL_CONTENT,HTTP_404_NOT_FOUND,HTTP_200_OK)


class signupview(APIView):
    permission_classes = [AllowAny]
    serializer_class = signupserializer
    def post(self,request):
        serializer= signupserializer(data=request.data)
        if serializer.is_valid():
             try:
                print('hai')
                serializer.save()
                print('hai')
                return Response({'status':'created'},status=HTTP_201_CREATED)
             except:
                return Response({'status':'not created','error':serializer.errors},status= HTTP_206_PARTIAL_CONTENT)    
        return Response({'status':'not created','error':serializer.errors},status= HTTP_206_PARTIAL_CONTENT) 
class loginview(APIView):
    permission_classes = [AllowAny]
    serializer_class = logserializer
    queryset = User.objects.all()
    def post(self,request):
        email = request.data.get('email')
        print(email)    
        password = request.data.get('password')
        try:
            user = authenticate(request,email = email,password = password)
            print(user.id)
        except:
             user=get_user_model()#go to setting and that define models is taken
             print(user)
             return Response({"status":"not-login"},status=HTTP_404_NOT_FOUND)
        if user:
            login(request,user)
            print('created')
            token,created = Token.objects.get_or_create(user=user)  
            data ={
                "token": token.key,
                'id':user.id}  
            return Response({'status':'login','data':data},status=HTTP_200_OK)



   













    