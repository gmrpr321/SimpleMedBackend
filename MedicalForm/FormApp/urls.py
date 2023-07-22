from django.urls import path
from .views import ApplicationFormListCreateView, ApplicationFormRetrieveUpdateView,ApplicationNoView

urlpatterns = [
    path('application-forms/no-of-student/',ApplicationNoView.as_view(),name='application-no-list'),
    path('application-forms/', ApplicationFormListCreateView.as_view(), name='application-form-list-create'),
    path('application-forms/<int:ar_number>', ApplicationFormRetrieveUpdateView.as_view(), name='application-form-retrieve-update'),
]
# urlpatterns = [
#     path('application-forms/', PostView.as_view(), name='application-form-list-create'),
#     path('application-forms/<int:pk>/', ApplicationFormRetrieveUpdateView.as_view(), name='application-form-retrieve-update'),
# ]

