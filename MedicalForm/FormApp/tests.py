from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from FormApp.models import ApplicationFormModel,CustomUser,AdmissionFormModel
from .serializers import ApplicationFormSerializer,AdmissionFormSerializer
User = CustomUser
class ApplicationFormCreateViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('application-create')
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='password'
        )
        self.valid_payload = {
            'email' : 'test@example.com',
            'student_name': 'John Doe',
            'course': 'Computer Science',
            'date_of_birth': '1990-01-01',
            'gender': 'Male',
            'is_hostellite': "",
            'community': 'OC',
            'religion': 'Christian',
            'native_place': 'City XYZ',
            'blood_group': 'O+',
            'height': '175.5',
            'weight': '70.2',
            'caste': 'General',
            'address_for_communication': '123 Main Street',
            'date_of_admission': '2023-01-01',
            'address_local_guardian': '456 Park Avenue',
            'nationality': 'Indian',
            'mother_tongue': 'English',
            'father_name': 'John Doe Sr.',
            'father_occupation': 'Engineer',
            'father_occupation_address': '789 Broadway',
            'father_phone_number': '1234567890',
            'father_email': 'john.doe@example.com',
            'mother_name': 'Jane Doe',
            'mother_occupation': 'Teacher',
            'mother_occupation_address': '321 Elm Street',
            'mother_phone_number': '9876543210',
            'mother_email': 'jane.doe@example.com',
            'student_contact_no': '9998887776',
            'student_email_id': 'john.doe@student.com',
            'mobile_1': '1112223334',
            'mobile_2': '5556667778',
            'mobile_3': '9990001112',
            'guardian_mobile': '4445556667',
            }


    def test_create_application_form(self):
        response = self.client.post(self.url, data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ApplicationFormModel.objects.count(), 1)
        self.assertEqual(ApplicationFormModel.objects.first().user, self.user)
        application_form_instance = ApplicationFormModel.objects.filter(student_contact_no=self.valid_payload['student_contact_no'])
        self.assertTrue(len(application_form_instance)>0)



class ApplicationFormUpdateTest(APITestCase):
    def setUp(self):
        # Create a user instance
        self.user = CustomUser.objects.create(email="example@example.com")

        # Create an application form instance
        self.application_form = ApplicationFormModel.objects.create(user=self.user, student_name="John Doe")

        # Define the URL for updating the application form
        self.url = reverse("application-update", kwargs={"pk": self.user.email})

        # Define the updated data
        self.updated_data = {
            "student_name": "Updated Student Name",
            "father_name": "Updated Father Name",
            # Add more fields to update as needed
        }

    def test_update_application_form(self):
        # Authenticate the user if needed
        self.client.force_authenticate(user=self.user)

        # Make a PUT request to update the application form
        response = self.client.put(self.url, data=self.updated_data)

        # Retrieve the latest application form instance from the database
        self.application_form.refresh_from_db()

        # Check the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the application form fields are updated correctly
        self.assertEqual(self.application_form.student_name, self.updated_data["student_name"])
        self.assertEqual(self.application_form.father_name, self.updated_data["father_name"])
        # Add more assertions for other fields as needed
class ApplicationFormRetriveTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="example@example.com")
        self.application_form = ApplicationFormModel.objects.create(user=self.user, student_name="John Doe",email="example@example.com")
        self.url = reverse("application-retrive", kwargs={"pk": self.user.email})

    def test_retrive_application_form(self):
        response = self.client.get(self.url)
        serializer = ApplicationFormSerializer(data =response.data)
        serializer.is_valid()
        print(serializer.errors,serializer.data)
        self.assertTrue(serializer.data["student_name"],self.application_form.student_name)
        
class AdmissionFormCreateTest(APITestCase):
    def setUp(self):
        # Create a user instance
        self.user = User.objects.create(
            username='testuser',
            email='example@example.com',
            password='password'
        )
        # Define the URL for creating an admission form
        self.url = reverse("admission-create")

        # Define the data for creating the admission form
        self.data = {
        "email": "example@example.com",
        "student_contact_no": "1234567890",
        "student_email_id": "example@example.com",
        "username": "example_username",
        "guardian_mobile": "9876543210",
        "father_name": "John Doe",
        "father_occupation": "Engineer",
        "father_occupation_address": "123 Main St, City",
        "father_phone_number": "9876543210",
        "father_email": "father@example.com",
        "mother_name": "Jane Doe",
        "mother_occupation": "Doctor",
        "mother_occupation_address": "456 Oak St, City",
        "mother_phone_number": "9876543210",
        "mother_email": "mother@example.com",
        "serial_no": "12345",
        "ar_number": "AR123",
        "date_of_admission": "2023-06-24",
        "admission_no": "A123",
        "student_name": "John Doe",
        "quota": "Govt",
        "date_of_birth": "2000-01-01",
        "community": "OC",
        "is_hostellite": "",
        "hsc_register_no": "HSC123",
        "board_of_study": "State",
        "neet_roll_no": "NEET123",
        "hsc_year_of_passing": 2022,
        "neet_year": 2022,
        "neet_study_center_name": "NEET Study Center",
        "no_of_neet_attempts": 2,
        "neet_air": 100,
        "selection_committee_allotment_order_no": "SC123",
        "selection_committee_general_rank": "SC Rank",
        "allotment_order_date": "2023-06-24",
        "neet_physics_mark": 100,
        "neet_chemistry_mark": 100,
        "neet_biology_mark": 100,
        "neet_total_mark": 300,
        "neet_physics_percentile": 99.99,
        "neet_chemistry_percentile": 99.99,
        "neet_biology_percentile": 99.99,
        "neet_total_percentile": 99.99,
        "hsc_physics_mark": 95.5,
        "hsc_chemistry_mark": 95.5,
        "hsc_biology_mark": 95.5,
        "hsc_total_mark": 286.5,
        "hsc_marks_maximum": 300,
        "pcb_percentage": 95.5,
}

    def test_create_admission_form(self):
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(AdmissionFormModel.objects.all())
        self.assertTrue(
            AdmissionFormModel.objects.count()>0
        )


class AdmissionFormUpdateTest(APITestCase):
    def setUp(self):
        # Create a user instance
        self.user = CustomUser.objects.create(email="example@example.com")

        # Create an application form instance
        self.application_form = AdmissionFormModel.objects.create(user=self.user, ar_number= "AR123",neet_air = 50)

        # Define the URL for updating the application form
        self.url = reverse("admission-update", kwargs={"pk": self.user.email})

        # Define the updated data
        self.updated_data = {
            "neet_physics_percentile": 99.99,
            "neet_chemistry_percentile": 99.99,
            "neet_biology_percentile": 99.99,
            "neet_air": 100,
            # Add more fields to update as needed
        }

    def test_update_application_form(self):
        # Authenticate the user if needed
        self.client.force_authenticate(user=self.user)

        # Make a PUT request to update the application form
        response = self.client.put(self.url, data=self.updated_data)

        # Retrieve the latest application form instance from the database
        self.application_form.refresh_from_db()

        # Check the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the application form fields are updated correctly
        self.assertEqual(self.application_form.neet_air, self.updated_data["neet_air"])
        # Add more assertions for other fields as needed
class AdmissionFormRetriveTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="example@example.com")
        self.admission_form = AdmissionFormModel.objects.create(user=self.user,email="example@example.com")
        self.url = reverse("admission-retrive", kwargs={"pk": self.user.email})

    def test_retrive_admission_form(self):
        response = self.client.get(self.url)
        serializer = AdmissionFormSerializer(data =response.data)
        serializer.is_valid()
        print(serializer.errors,serializer.data)
        self.assertTrue(serializer.data["email"],self.admission_form.email)