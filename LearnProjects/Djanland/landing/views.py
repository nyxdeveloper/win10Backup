from django.shortcuts import render
from django.views import View
from .models import *


class HomeView(View):
    def get(self, request):
        blocks = Block.objects.all()
        header = Header.objects.last()
        footer = Footer.objects.last()
        headersLinks = HeadersLink.objects.all()
        return render(request, 'home.html', {
            'blocks': blocks,
            'header': header,
            'headersLinks': headersLinks,
            'footer': footer
        })
