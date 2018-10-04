from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from forum.models import Section


# Create your views here.
# def homepage(request):
#     return render(request, 'core/homepage.html')

class HomeView(ListView):
    queryset = Section.objects.all()
    template_name = 'core/homepage.html'
    context_object_name = "list_section"

class UserList(LoginRequiredMixin, ListView):
    model = User
    context_object_name = ''
    template_name='core/users.html'

def userProfileView(request, username):
    user = get_object_or_404(User, username=username)
    context ={"user": user}
    return render(request, 'core/user_profile.html', context)

