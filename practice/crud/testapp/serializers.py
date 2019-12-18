from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from testapp.models import Question
class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('id','first_name','last_name','email','url')
    
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=['title','status','created_by']
    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self,data):
        username=data.get('username')
        password=data.get('password')

        if username and password:
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data['user']=user
                else:
                    msg='user is deactivated'
                    raise exceptions.ValidationError(msg)
            else:
                msg='unable to login with given credencials'
                raise exceptions.ValidationError(msg)
        else:
            msg='must provide username and password'
            raise exceptions.ValidationError(msg)
        return data