from django.http import HttpResponse
from django.shortcuts import render

def segundo_template(request):
    return render(request, 'template_2.html', context={})