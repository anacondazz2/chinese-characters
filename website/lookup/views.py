from django.shortcuts import render
from django.http import HttpResponse
from .parser import main
from .models import Word


def index(request):
    return HttpResponse("Hello, world.")


def print_dict(request):
    # Test the output of the parser.
    return HttpResponse("Testing...")


def lookup_entry(request):
    query = request.GET.get('query', '')
