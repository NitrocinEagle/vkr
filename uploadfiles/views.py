from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

from .forms import ArticleForm


def Upload_file(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/theory/all')
  else:
    form = ArticleForm()

  return render(request, 'file_upload.html', {'form': form})