from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from testapp.serializers import LoginSerializer
from django.contrib.auth import login,logout
from rest_framework.authtoken.models import Token 
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class LoginView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        login(request,user)
        token, created=Token.objects.get_or_create(user=user)
        return Response({'token':token.key},status=200)



class LogOutView(APIView):
    authentication_classes=(TokenAuthentication,)

    def post(self,request):
        logout(request)
        return Response(status=204)

    
