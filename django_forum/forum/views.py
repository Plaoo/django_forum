from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Section

class CreateSection(CreateView):
    model = Section
    fields = "__all__"
    template_name = "forum/create_section.html"
    success_url = "/"