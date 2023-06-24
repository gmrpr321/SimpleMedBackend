from rest_framework import serializers
from .models import ApplicationFormModel,AdmissionFormModel,CustomUser
User = CustomUser
class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationFormModel
        fields = "__all__"
        extra_kwargs = {
            'user': {'required': False}
        }
    def create(self, validated_data):
        print(validated_data)
        email = validated_data.pop('email')
        user_instance = User.objects.get(email=email)
        application_instance = ApplicationFormModel(**validated_data,user=user_instance)
        application_instance.save()
        return application_instance
    
    def update(self,instance,validated_data):
        for field in validated_data:
            setattr(instance,field,validated_data[field])
        instance.save()
        return instance

class AdmissionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionFormModel
        fields = "__all__"
        extra_kwargs = {
            'user': {'required': False}
        }
    def create(self, validated_data):
        email = validated_data.pop('email')
        user_instance = User.objects.get(email=email)
        admission_instance = AdmissionFormModel(**validated_data,user=user_instance)
        admission_instance.save()
        return admission_instance
    
    def update(self,instance,validated_data):
        for field in validated_data:
            setattr(instance,field,validated_data[field])
        instance.save()
        return instance
    