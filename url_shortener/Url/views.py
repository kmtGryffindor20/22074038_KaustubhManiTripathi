from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.views.generic import RedirectView, DetailView, CreateView, ListView
from .models import Urls
from django.http import Http404
import string
import random


# Create your views here.

def shorten_url():
    letters = string.ascii_letters
    shortened_url = f"surl.{''.join(random.choice(letters) for _ in range(5))}"

    return shortened_url

class RedirectToLongURLView(RedirectView):

    permanent = True
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        short_url = kwargs['s_url']
        long_url = Urls.objects.filter(short_url=short_url).first()
        if long_url is not None:
            return long_url.long_url
        raise Http404("The url you are trying to access is either wrong or does not exists.")
    
class URLShorteningView(CreateView):
    model = Urls
    success_url = "url/shortened/"
    fields = ['long_url']

    def form_valid(self, form: BaseModelForm):
        shortened_url = shorten_url()
        while Urls.objects.filter(short_url=shortened_url).exists():
            shortened_url = shorten_url()
        form.instance.short_url = shortened_url
        return super().form_valid(form)

    
class URLShortenedSuccessView(DetailView):

    model = Urls
    def get_object(self):
        return Urls.objects.last()
    

class URListView(ListView):

    model = Urls
    context_object_name = 'urls'
    
    

    
    
    
    
    
        