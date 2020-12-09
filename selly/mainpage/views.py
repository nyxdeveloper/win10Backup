from django.shortcuts import render
from django.views.generic.base import View


class MainpageView(View):
    def get(self, request):
        return render(request, 'mainpage.html')