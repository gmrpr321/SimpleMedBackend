import os
import io
from PIL import Image
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ApplicationFormModel
from django.core.files.uploadedfile import SimpleUploadedFile
from .serializers import ApplicationModelSerializer
class ApplicationFormTests(APITestCase):
    def test_create_application_form(self):
        url = reverse('application-form-list-create')
    
        # Create sample image and PDF files for testing
        app_directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(app_directory, 'testFiles', 'dummy.jpg')
        pdf_path = os.path.join(app_directory, 'testFiles', 'dummy.pdf')

        with open(image_path, 'rb') as image_file, open(pdf_path, 'rb') as pdf_file:
            image_data = SimpleUploadedFile("dummy.jpg", image_file.read(), content_type="image/jpeg")
            pdf_data = SimpleUploadedFile("dummy.pdf", pdf_file.read(), content_type="application/pdf")

            data = {
                'email': 'test@example.com',
                'student_name': 'John Doe',
                'course': 'Engineering',
                'date_of_birth': '1990-01-01',
                'gender': 'Male',
                'is_hostellite': "Day Scholar",
                'community': 'OC',
                'religion': 'Christian',
                'native_place': 'New York',
                'blood_group': 'O+',
                'height': 180.5,
                'weight': 75.0,
                'caste': 'General',
                'address_for_communication': '123 Main Street',
                'student_contact_no': '9876543210',
                'mobile_1': '1234567890',
                'mobile_2': '9876543210',
                'mobile_3': '9998887776',
                'date_of_admission': '2023-01-01',
                'address_local_guardian': '456 Park Avenue',
                'guardian_mobile': '8887776665',
                'nationality': 'American',
                'mother_tongue': 'English',
                'quota': 'General',
                'father_name': 'John Doe Sr.',
                'father_occupation': 'Engineer',
                'father_occupation_address': '789 Elm Street',
                'father_phone_number': '1112223334',
                'father_email': 'father@example.com',
                'mother_name': 'Jane Doe',
                'mother_occupation': 'Teacher',
                'mother_occupation_address': '789 Elm Street',
                'mother_phone_number': '1112223335',
                'mother_email': 'mother@example.com',
                'hsc_register_no': '12345678',
                'board_of_study': 'State',
                'hsc_year_of_passing': 2022,
                'hsc_physics_mark': 95.5,
                'hsc_chemistry_mark': 90.0,
                'hsc_biology_mark': 92.0,
                'hsc_total_mark': 277.5,
                'hsc_marks_maximum': 300.0,
                'pcb_percentage': 92.5,
                'neet_roll_no': 'NEET1234',
                'neet_year': 2022,
                'neet_study_center_name': 'Medical Academy',
                'no_of_neet_attempts': 2,
                'neet_air': 500,
                'selection_committee_allotment_order_no': 'ORDER123',
                'selection_committee_general_rank': 'RANK123',
                'allotment_order_date': '2022-12-31',
                'neet_physics_mark': 170,
                'neet_chemistry_mark': 175,
                'neet_biology_mark': 165,
                'neet_total_mark': 510,
                'neet_physics_percentile': 95.5,
                'neet_chemistry_percentile': 90.0,
                'neet_biology_percentile': 92.0,
                'neet_total_percentile': 87.5,
                'student_photo': image_data,
                'neet_score_card': pdf_data,
                'conduct_certificate': pdf_data,
                'neet_admit_card': pdf_data,
                'allotment_order_sslc_certificate': pdf_data,
                'hsc_certificate': pdf_data,
                'transfer_certificate': pdf_data,
                'community_certificate': pdf_data,
                'aadhar_card': pdf_data,
                'eligibility_migration_certificates': pdf_data,
                'nativity_certificate': pdf_data,
                'income_certificate': pdf_data,
                'physical_fitness_certificate': pdf_data,
                'declaration_form': pdf_data,
                'anti_ragging_bond': pdf_data,
                'physically_handicapped_certificate': pdf_data,
            }

            response = self.client.post(url, data, format='multipart')
            serializer = ApplicationModelSerializer(data=data)
            serializer.is_valid()
            print(serializer.errors)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
