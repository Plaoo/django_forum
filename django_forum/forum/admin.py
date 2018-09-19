from django.contrib import admin
from .models import Section, Discussion, Post

class DiscussionModelAdmin(admin.ModelAdmin):
    model = Discussion
    list_display = ["title", "section_membership", "author"]
    search_fields = ["title", "author"]
    list_filter = ["section_membership", "data_creation"]

class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["discussion", "author_post"]
    search_fields = ["content"]
    list_filter = ["author_post", "data_creation"]

class SectionModelAdmin(admin.ModelAdmin):
    model = Section
    list_display = ["name_section", "description"]

admin.site.register(Section, SectionModelAdmin)
admin.site.register(Discussion, DiscussionModelAdmin)
admin.site.register(Post, PostModelAdmin)