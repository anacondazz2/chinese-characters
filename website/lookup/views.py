from django.shortcuts import render
from django.http import HttpResponse
# Testing parser...
from .parser import parsed_dict


def index(request):
    return HttpResponse("Hello, world.")


def test(request):
    # Test the output of the parser.
    print(parsed_dict)
    return HttpResponse("Testing...")
