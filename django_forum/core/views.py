from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from forum.models import Discussion, Section, Post


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
    discussion_user = Discussion.objects.filter(author = user).order_by("-pk")
    context ={"user": user, "discussion_user":discussion_user}
    return render(request, 'core/user_profile.html', context)

def search(request):
    if "q" in request.GET:
        querystring = request.GET.get("q")
        if len(querystring) == 0:
            return redirect("/search/")
        discussions = Discussion.objects.filter(title__icontains=querystring)
        posts = Post.objects.filter(content__icontains=querystring)
        users = User.objects.filter(username__icontains=querystring)
        context = {"discussions":discussions,
                   "posts":posts,
                   "users":users}
        return render(request, 'core/search.html', context)
    else:
        return render(request, 'core/search.html')

