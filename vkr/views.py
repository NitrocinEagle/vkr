from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.

def main(request):
    view = "main"
    html = "<html><body> This is %s view</body></html>" % view
    return HttpResponse(html)

def index(request):
    view = 'SFU'
    t = get_template('index.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)