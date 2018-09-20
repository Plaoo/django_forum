from django.urls import path
from . import views

urlpatterns = [
    path('new_section/', views.CreateSection.as_view(), name="create_section"),
    path('section/<int:pk>/', views.ViewSection, name="view_section")
]
