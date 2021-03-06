from django.urls import path
from . import views

urlpatterns = [
    path('new_section/', views.CreateSection.as_view(), name="create_section"),
    path('section/<int:pk>/', views.viewSection, name="view_section"),
    path('section/<int:pk>/create_discussion/', views.createDiscussion, name="create_discussion"),
    path('discussion/<int:pk>/', views.viewDiscussion, name="view_discussion"),
    path('discussion/<int:pk>/reply/', views.addReply, name="reply_discussion"),
    path('discussion/<int:id>/remove_post/<int:pk>/', views.DeletePost.as_view(), name="delete_post"),


]
