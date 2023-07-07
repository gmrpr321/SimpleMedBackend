from rest_framework import serializers
from .models import ApplicationFormModel

class ApplicationModelSerializer(serializers.ModelSerializer):
    student_photo = serializers.ImageField(required=False)
    neet_score_card = serializers.FileField(required=False)
    conduct_certificate = serializers.FileField(required=False)
    neet_admit_card = serializers.FileField(required=False)
    allotment_order_sslc_certificate = serializers.FileField(required=False)
    hsc_certificate = serializers.FileField(required=False)
    transfer_certificate = serializers.FileField(required=False)
    community_certificate = serializers.FileField(required=False)
    aadhar_card = serializers.FileField(required=False)
    eligibility_migration_certificates = serializers.FileField(required=False)
    nativity_certificate = serializers.FileField(required=False)
    income_certificate = serializers.FileField(required=False)
    physical_fitness_certificate = serializers.FileField(required=False)
    declaration_form = serializers.FileField(required=False)
    anti_ragging_bond = serializers.FileField(required=False)
    physically_handicapped_certificate = serializers.FileField(required=False)

    class Meta:
        model = ApplicationFormModel
        exclude = ("ar_number",)

    def create(self, validated_data):
        instance = super().create(validated_data)
        field_mapping = {
            'student_photo': 'student_photo.jpg',
            'neet_score_card': 'neet_score_card.pdf',
            'conduct_certificate': 'conduct_certificate.pdf',
            'neet_admit_card': 'neet_admit_card.pdf',
            'allotment_order_sslc_certificate': 'allotment_order_sslc_certificate.pdf',
            'hsc_certificate': 'hsc_certificate.pdf',
            'transfer_certificate': 'transfer_certificate.pdf',
            'community_certificate': 'community_certificate.pdf',
            'aadhar_card': 'aadhar_card.pdf',
            'eligibility_migration_certificates': 'eligibility_migration_certificates.pdf',
            'nativity_certificate': 'nativity_certificate.pdf',
            'income_certificate': 'income_certificate.pdf',
            'physical_fitness_certificate': 'physical_fitness_certificate.pdf',
            'declaration_form': 'declaration_form.pdf',
            'anti_ragging_bond': 'anti_ragging_bond.pdf',
            'physically_handicapped_certificate': 'physically_handicapped_certificate.pdf',
        }

        for field_name, filename in field_mapping.items():
            file_data = validated_data.pop(field_name, None)
            if file_data:
                file_field = getattr(instance, field_name)
                file_field.name = f"{instance.ar_number}_{filename}"
                setattr(instance, field_name, file_field)

        instance.save()
        return instance