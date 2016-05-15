from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from vkr.models import theory


# Create your views here.

def home(request):
    view = 'SFU'
    return render_to_response('index.html', {'name': view})


def allTheory(request):
    return render_to_response('allTheory.html', {'allTheory': theory.objects.all()})


def oneTheory(request, theory_id):
    return render_to_response('oneTheory.html', {'oneTheory': theory.objects.get(id=theory_id)})
