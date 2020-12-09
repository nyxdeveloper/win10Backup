from django import forms
from django.forms import ModelForm
from .models import *


# class QuestionForm(ModelForm):
#     class Meta:
#         model = Question
#         fields = ['name', 'mail', 'question']

class QuestionForm(forms.Form):
    name = forms.CharField(max_length=100)
    Email = forms.EmailField()
    question = forms.CharField(widget=forms.Textarea)

    def save(self):
        new_question = Question.objects.create(
            name=self.cleaned_data['name'],
            mail=self.cleaned_data['Email'],
            question=self.cleaned_data['question']
        )
        return new_question
