from rest_framework import generics
from .models import ApplicationFormModel
from .serializers import ApplicationModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

class ApplicationFormListCreateView(generics.ListCreateAPIView):
    queryset = ApplicationFormModel.objects.all()
    serializer_class = ApplicationModelSerializer

    def create(self, request, *args, **kwargs):
        print('asdf')
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            print(e.detail)
        print('d')
        print(serializer.errors,'asdf',serializer)  # Print the errors to the console
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ApplicationFormRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ApplicationFormModel.objects.all()
    serializer_class = ApplicationModelSerializer