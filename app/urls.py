from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('formpage/', views.FormView.as_view(),name="formpage"),
    path('doui/', views.ChoiceView.as_view(), name="doui"),
]
