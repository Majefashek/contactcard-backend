
from django.views import View
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import OuterRef, Exists
import ast
from .serializers import UserSerializer
from . models import User
from django.contrib.auth import authenticate, login
import jwt
from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication 



class LoginAPIEndpoint(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)

            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response({
                'status': 200,
                'message': 'Login successful',
                'token': token
            })
           
            # Generate or retrieve an authentication token
               
        else:
            return Response({
                'status': 404,
                'message': 'Invalid credentials'
            })







class SignUpAPIEndpoint(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


       


class RetrieveUserEndpoint(generics.RetrieveAPIView):
    
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=User.objects.get(id=request.user.id)
        serialized_user=UserSerializer(user).data
        return Response({'message':'Successfully retrieved',
                         'data':serialized_user})

   
   

class UpdateUserInfoEndpoint(generics.UpdateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=User.objects.all()
    serializer_class=UserSerializer

    pass

class DeleteUserInfo(generics.DestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset=User.objects.all()
    serializer_class=UserSerializer

       

