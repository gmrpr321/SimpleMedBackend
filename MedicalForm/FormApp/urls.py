from django.urls import path
from .views import ApplicationFormListCreateView, ApplicationFormRetrieveUpdateView

urlpatterns = [
    path('application-forms/', ApplicationFormListCreateView.as_view(), name='application-form-list-create'),
    path('application-forms/<int:pk>/', ApplicationFormRetrieveUpdateView.as_view(), name='application-form-retrieve-update'),
]
