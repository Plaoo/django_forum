from django import forms

from .models import Discussion, Post

class DiscussionModelForm(forms.ModelForm):
    content = forms.CharField(
        widget = forms.Textarea(attrs={"placeholder": "Your text here"}),
        max_length=5000, label="First Message"
    )

    class Meta:
        model = Discussion
        fields = ["title", "content"]
        widgets = {"title":forms.TextInput(attrs={"placeholder": "Title"})
        }

class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["content"]
        widgets ={
            "content": forms.Textarea(attrs={'rows': 5,})
        }
        labels ={
            "content": "Message"
        }