from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import User
from .serializer import signupserializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.status import(
    HTTP_100_CONTINUE,HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_206_PARTIAL_CONTENT)


class signupview(APIView):
    permission_classes = [AllowAny]
    serializer_class = signupserializer
    def post(self,request):
        serializer= signupserializer(data=request.data)
        if serializer.is_valid():
             try:
                serializer.save()
                return Response({'status':'created'},status=HTTP_201_CREATED)
             except:
                return Response({'status':'not created','error':serializer.errors},status= HTTP_206_PARTIAL_CONTENT)    
        return Response({'status':'not created','error':serializer.errors},status= HTTP_206_PARTIAL_CONTENT) 


       
       

























        # if user_form.is_valid() :
        #   
        #     user = user_form.save(commit=False)
        #     user.password = make_password(user.password)
        #     user.save()
 



#   serializer.save()
#             return Response({'status':'created'},status=HTTP_201_CREATED)
#         return Response({'status':'not created','error':serializer.errors},status= HTTP_206_PARTIAL_CONTENT) 































# class Signupview(CreateAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = signupserializer
#     def create(self,request):
#         serializer = signupserializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({'status':'suceessfully'},status=HTTP_201_CREATED)
#         return Response({'status':'uncuceessful'},status=HTTP_400_BAD_REQUEST)

# # # class usercreate(APIView):
# #     permission_classes = [IsAuthenticated]
# #     serializer_class = userserializer
# #     def get(self,request):
# #         try:
# #             data = User.objects.all()
# #             serializer = userserializer(data)
# #             return Response({'status':'suceessful','data':serializer.data})
# #         except:
# #             return Response({'status':'unsucessful','error':serializer.errors},status=HTTP_400_BAD_REQUEST)
# #     def post(self,request):
# #         serializer = userserializer(data=request.data)
# #         if serializer.is_valid:
# #             serializer.save()
# #             return Response({'status':'cretaed','data':serializer.data},status=HTTP_201_CREATED)
# #         return Response({'status':'notcreate','error':serializer.errors},status=HTTP_400_BAD_REQUEST)
# class SignupView(APIView):
#     permission_classes = [AllowAny]
#     serializer_class = signupserializer
#     def post(self,request):
#         serializer = signupserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':'suceessfuliysigned','data':serializer.data},status=HTTP_201_CREATED)
#         return Response({'status':'unsceesful','error':serializer.errors},status=HTTP_400_BAD_REQUEST) 
    
    
# class LoginView(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class =   logserializer
#     def post(self,request):
#         serializer = logserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':'loginsuceesfuly','data':serializer.data},status=HTTP_201_CREATED)
#         return Response({'status':'error','error':serializer.errors},status=HTTP_400_BAD_REQUEST)       
    
    
    
#     #  if ('password' in self.request.data):
#     #         password = make_password(self.request.data['password'])
#     #         serializer.save(password=password)
#     #         serializer.is_valid()
#     #         # serializer.save()
        