from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Word
from .serializers import WordSerializer


def index(request):
    return Response({})


def print_dict(request):
    # Test the output of the parser.
    return Response({})


@api_view(['GET'])
def lookup_entry(request):
    print("in")
    query = request.GET.get('query', '')
    if query:
        print(1)
        word_instances = Word.objects.filter(pinyin__icontains=query)
        if word_instances.exists():
            serializer = WordSerializer(word_instances, many=True)
            return Response(serializer.data)
    else:
        print(2)
    return Response({'error': 'No entries found'}, status=404)
