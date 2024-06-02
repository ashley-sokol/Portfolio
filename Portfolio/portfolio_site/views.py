import base64
import boto3
from django import template
from django.http import HttpResponse, HttpResponseRedirect, Http404, FileResponse
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.views import generic, View
from django.urls import reverse
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth import logout
import uuid

class IndexView(View):
    def get(self, request):
        return render(request, 'portfolio_site/index.html')
