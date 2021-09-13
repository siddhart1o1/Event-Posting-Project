from django import forms
from django.forms import ModelForm
from .models import Post

class EventForm(ModelForm):
    class Meta:
        model = Post
        fields = ("title","date","location","time","image")
        widgets = {
            "title":forms.TextInput(attrs={"class": "form-control"}),
            "date":forms.DateInput(attrs={"class": "form-control"}),
            "location":forms.TextInput(attrs={"class": "form-control"}),
            "time":forms.TimeInput(attrs={"class": "form-control"}),
            "image":forms.FileInput(attrs={"class": "form-control"}),

        }

