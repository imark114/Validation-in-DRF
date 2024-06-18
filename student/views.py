from django.shortcuts import render
import io
from .models import Student
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentApiViw(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            data = serializer.data
            return JsonResponse(data, safe=False)
        
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            data = serializer.data
            return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Inserted Successfull'}
            return JsonResponse(res)
        else:
            return JsonResponse(serializer.errors)
    
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Completely Updated'}
            return JsonResponse(res, safe=False)
        else:
            return JsonResponse(serializer.errors)

    def patch(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Partically Updated'}
            return JsonResponse(res, safe=False)
        else:
            return JsonResponse(serializer.errors)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Deleted Succefull'}
        return JsonResponse(res, safe=False)




