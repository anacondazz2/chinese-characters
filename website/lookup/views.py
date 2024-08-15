from django.shortcuts import render
from django.http import HttpResponse
from .parser import list_of_dicts


def index(request):
    return HttpResponse("Hello, world.")


def print_dict(request):
    # Test the output of the parser.
    print(list_of_dicts)
    return HttpResponse("Testing...")
