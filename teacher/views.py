from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class AddTeacherAPIView(APIView):
    def post(self, request):
        teacher_serializer = AddTeacherSerializer(data=request.data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return Response({'message': 'Teacher registred succesfully.'})
        return Response({'message': teacher_serializer.errors})
    
class ClassAPIView(APIView):
    def get(self, request, class_id):
        class_serialzer = 
    



