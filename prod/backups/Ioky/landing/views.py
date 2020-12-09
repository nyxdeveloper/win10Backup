from django.shortcuts import render, redirect
from django.views import View
from . import models
from .forms import QuestionForm


class HomePageRu(View):
    def get(self, request):
        questionForm = QuestionForm()
        questions = models.Question.objects.all()
        return render(request, 'index.html', {
            'questions': questions,
            'questionForm': questionForm
        })


class HomePageEn(View):
    def get(self, request):
        questionForm = QuestionForm()
        questions = models.Question.objects.all()
        return render(request, 'english.html', {
            'questions': questions,
            'questionForm': questionForm
        })


class CreateQuestion(View):
    def post(self, request):
        boundForm = QuestionForm(request.POST)
        if boundForm.is_valid():
            new_question = boundForm.save()
            return redirect('/')
        return render(request, 'index.html')
