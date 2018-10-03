from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Section, Post, Discussion
from .mixins import StaffMixing
from .forms import DiscussionModelForm

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

@login_required
def createDiscussion(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == "POST":
        form = DiscussionModelForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit = False)
            discussion.section_parent = section
            discussion.author = request.user
            discussion.save()
            first_post = Post.objects.create(discussion = discussion, 
                                             author_post=request.user,
                                             content = form.cleaned_data["content"]
                                            )
            return HttpResponseRedirect("/admin")
            
    else:
        form = DiscussionModelForm()
    context = {"form":form,
               "section":section}

    return render(request, "forum/create_discussion.html", context)

def viewDiscussion(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    posts_discussion = Post.objects.filter(discussion=discussion)
    context = {"discussion":discussion, "posts_discussion":posts_discussion}
    return render(request, "forum/single_discussion.html", context)