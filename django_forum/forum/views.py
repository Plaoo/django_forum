from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Section
from .mixins import StaffMixing

class CreateSection(StaffMixing, CreateView):
    model = Section
    fields = "__all__"
    template_name = "forum/create_section.html"
    #return to homepage after create a section
    success_url = "/"