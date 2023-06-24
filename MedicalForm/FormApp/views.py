from django.shortcuts import render
from .serializers import ApplicationFormSerializer,AdmissionFormSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser,ApplicationFormModel,AdmissionFormModel

User = CustomUser
class ApplicationFormCreateView(APIView):
    def post(self, request):
        serializer = ApplicationFormSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.errors)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print( serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationFormUpdateView(APIView):
    def put(self, request, pk):
        user = User.objects.get(email=pk)
        application_instance = user.ApplicationForm
        serializer = ApplicationFormSerializer(application_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)

class ApplicationFormRetriveView(APIView):
    def get(self,request,pk):
        try:
            application_instance = ApplicationFormModel.objects.get(email=pk)
            serializer = ApplicationFormSerializer(application_instance)
            return Response(serializer.data)
        except:
            return Response(status=404)

class AdmissionFormCreateView(APIView):
    def post(self, request):
        serializer = AdmissionFormSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.errors)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.error_messages, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdmissionFormUpdateView(APIView):
    def put(self, request, pk):
        user = User.objects.get(email=pk)
        admission_instance = user.AdmissionForm
        serializer = AdmissionFormSerializer(admission_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)

class AdmissionFormRetriveView(APIView):
    def get(self,request,pk):
        try:
            admission_instance = AdmissionFormModel.objects.get(email=pk)
            serializer = AdmissionFormSerializer(admission_instance)
            return Response(serializer.data)
        except:
            return Response(status=404)
    
class CreateUserView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        username = request.data.get("username")

        try:
            User.objects.create(username=username, email=email, password=password)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class LoginUserView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, password=password, email=email)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_200_OK)


class LogoutUserView(APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
