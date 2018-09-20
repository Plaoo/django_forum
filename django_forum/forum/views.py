from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Section
from .mixins import StaffMixing

class CreateSection(StaffMixing, CreateView):
    model = Section
    fields = "__all__"
    template_name = "forum/create_section.html"
    #return to homepage after create a section
    success_url = "/"


def ViewSection(request, pk):
    section = get_object_or_404(Section, pk=pk)
    context = {"section": section}
    return render(request, "forum/single_section.html", context)
