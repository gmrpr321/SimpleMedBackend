from rest_framework import generics
from .models import ApplicationFormModel
from .serializers import ApplicationModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

class ApplicationFormListCreateView(generics.ListCreateAPIView):
    queryset = ApplicationFormModel.objects.all()
    serializer_class = ApplicationModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            None
        print(serializer.errors)  # Print the errors to the console
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(list(ApplicationFormModel.objects.all())[-1].ar_number)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ApplicationFormRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ApplicationFormModel.objects.all()
    serializer_class = ApplicationModelSerializer
    lookup_field = "ar_number"

    def update(self, request, *args, **kwargs):
        print("yess")
        try:
            instance = ApplicationFormModel.objects.get(ar_number=kwargs['ar_number'])
            serializer = ApplicationModelSerializer(instance, data=request.data, partial=True)
            serializer.is_valid()
            print(instance.ar_number)
            print(serializer.errors)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

# class PostView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def get(self, request, *args, **kwargs):
#         posts = ApplicationFormModel.objects.all()
#         serializer = ApplicationModelSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
        
#         posts_serializer = ApplicationModelSerializer(data=request.data)
#         print("asdfasdf")
#         if posts_serializer.is_valid():
#             print(posts_serializer.errors)
#             posts_serializer.save()
            
#             return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print('error', posts_serializer.errors)
#             return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)