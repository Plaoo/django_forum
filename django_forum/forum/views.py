from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator
from .mixins import StaffMixing
from .models import Discussion, Post, Section
from .forms import DiscussionModelForm, PostModelForm

class CreateSection(StaffMixing, CreateView):
    model = Section
    fields = "__all__"
    template_name = "forum/create_section.html"
    #return to homepage after create a section
    success_url = "/"


def viewSection(request, pk):
    section = get_object_or_404(Section, pk=pk)
    discussion_section = Discussion.objects.filter(section_membership=section).order_by("-data_creation")
    context = {"section": section, "discussion":discussion_section}
    return render(request, "forum/single_section.html", context)

@login_required
def createDiscussion(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == "POST":
        form = DiscussionModelForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit = False)
            discussion.section_membership = section
            discussion.author = request.user
            discussion.save()
            first_post = Post.objects.create(discussion = discussion, 
                                             author_post=request.user,
                                             content = form.cleaned_data["content"]
                                            )
            return HttpResponseRedirect(discussion.get_absolute_url())
            
    else:
        form = DiscussionModelForm()
    context = {"form":form,
               "section":section}

    return render(request, "forum/create_discussion.html", context)

@login_required
def viewDiscussion(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)
    posts_discussion = Post.objects.filter(discussion=discussion)

    paginator = Paginator(posts_discussion, 5)
    page = request.GET.get("pages")
    posts = paginator.get_page(page)

    form_reply = PostModelForm()
    context = {"discussion":discussion, 
                "posts_discussion":posts, 
                "form_reply":form_reply}
    return render(request, "forum/single_discussion.html", context)

def addReply(request, pk):
    discussion = get_object_or_404(Discussion, pk=pk)

    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save(commit= False)
            form.instance.discussion = discussion
            form.instance.author_post = request.user
            form.save()
            url_discussion = reverse("view_discussion", kwargs={'pk': pk})
            pages_in_discussion = discussion.get_n_pages()
            if pages_in_discussion > 1:
                success_url = url_discussion + "?pages=" + str(pages_in_discussion)
                return HttpResponseRedirect(success_url)
            else:
                return HttpResponseRedirect(url_discussion)
    else:
        HttpResponseBadRequest()

class DeletePost(DeleteView):
    model = Post
    success_url = "/"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author_post_id=self.request.user.id)
