from django.urls import path
from . import views

urlpatterns = [
    path('formpage/', views.FormView.as_view(),name="formpage"),
    path('doui/', views.Index.as_view(), name="doui"),
]
