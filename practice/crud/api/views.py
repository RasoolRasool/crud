from django.shortcuts import render
from rest_framework import viewsets
from testapp.serializers import EmployeeSerializers,QuestionSerializer
from django.contrib.auth.models import User
from testapp.models import Question
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
import io
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=EmployeeSerializers

@api_view(['GET','POST'])
def Poll(request):
    if request.method=="GET":
        questions=Question.objects.all()
        serializer=QuestionSerializer(questions,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="POST":
        data = JSONParser().parse(request)
        serializer=QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def Poll_Detail(request,id):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    try:
        question=Question.objects.get(id=id)
    except Question.DoesNotExist:
        return HttpResponse(status=404)
    if request.method=="GET":
        serializer=QuestionSerializer(question)
        return JsonResponse(serializer.data)
    elif request.method=="PUT":
        data=JSONParser().parse(request)
        serializer=QuestionSerializer(question,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method=="DELETE":
        question.delete()
        return HttpResponse(status=204)

class Employee_list(APIView):
    def get(self,request):
        emp=Question.objects.all()
        serializer=QuestionSerializer(emp,many=True)
        return JsonResponse(serializer.data,safe=False)

    def post(self,request):
        data=JSONParser().parse(request)
        serializer=QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
