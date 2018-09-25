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
