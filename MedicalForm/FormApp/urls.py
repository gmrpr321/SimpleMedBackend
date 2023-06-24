from django.urls import path
from .views import AdmissionFormCreateView,ApplicationFormCreateView,AdmissionFormUpdateView,ApplicationFormUpdateView,CreateUserView,LoginUserView,LogoutUserView,AdmissionFormRetriveView,ApplicationFormRetriveView

urlpatterns = [
    path("application-form-create/",ApplicationFormCreateView.as_view(),name="application-create"),
    path("admission-form-create/",AdmissionFormCreateView.as_view(),name='admission-create'),
    path("application-form-update/<str:pk>",ApplicationFormUpdateView().as_view(),name='application-update'),
    path("admission-form-update/<str:pk>",AdmissionFormUpdateView.as_view(),name='admission-update'),
    path("application-form-retrive/<str:pk>",ApplicationFormRetriveView.as_view(),name="application-retrive"),
    path("admission-form-retrive/<str:pk>",AdmissionFormRetriveView.as_view(),name="admission-retrive"),
    path("user-create/", CreateUserView.as_view(),name = 'create-user'),
    path("user-login/", LoginUserView.as_view(),name = 'login-user'),
    path("user-logout/", LogoutUserView.as_view(),name = 'logout-user'),
]
