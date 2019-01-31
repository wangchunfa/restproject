from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from drest.serializers import UserSerializer
from rest_framework.decorators import api_view
from .models import User
from .services import UserService


@api_view(['GET'])
def list_user(request):
    user_obj = User.objects.all()
    serializer = UserSerializer(user_obj, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def add_user(request):
    data = JSONParser().parse(request)
    user_service = UserService()
    ret_data = user_service.add_user(data=data)
    return JsonResponse(ret_data, status=200)


@api_view(['POST'])
def del_user(request):
    data = JSONParser().parse(request)
    User.objects.filter(id=data['id']).delete()
    return JsonResponse({"msg": "Delete Success", "code": 200}, status=200)

