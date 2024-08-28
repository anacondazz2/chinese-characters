from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Word
from .serializers import WordSerializer
import re
import unicodedata


def print_dict(request):
    # Test the output of the parser.
    return Response({})


def is_chinese_char(char):
    # Get the Unicode block name
    block_name = unicodedata.name(char, None)
    if block_name is None:
        return False
    # Check if the block name indicates a Chinese character
    return 'CJK UNIFIED IDEOGRAPHS' in block_name or \
           'CJK COMPATIBILITY IDEOGRAPHS' in block_name or \
           'CJK UNIFIED IDEOGRAPHS EXTENSION' in block_name or \
           'CJK RADICALS SUPPLEMENT' in block_name


def build_regex_pattern(query):
    parts = query.split()
    pattern = ''
    if len(parts) == 1:
        pattern = r'^' + re.escape(parts[0]) + r'[a-zA-Z]*[1-5]?$'
    else:
        last = re.escape(parts[-1]) + r'[a-zA-Z]*[1-5]?$'
        rest = r'^' + ' '.join(
            [f'{re.escape(part)}[1-5]?' for part in parts[:-1]])
        pattern = rest + ' ' + last
        # print(rest)
        # print(last)
        # print(pattern)
    return pattern


@api_view(['GET'])
def lookup_entry(request):
    print("in lookup_entry view")
    query = request.GET.get('query', '')
    if query:
        if is_chinese_char(query[0]):
            pattern = build_regex_pattern(query)
            word_instances = Word.objects.filter(pinyin__regex=pattern)
            if word_instances.exists():
                print("word_instances exists")
                serializer = WordSerializer(word_instances, many=True)
                return Response(serializer.data)
        else:
            pattern = r'^' + query + r'$'
            word_instances = Word.objects.filter(simplified__regex=pattern)
            if word_instances.exists():
                print("word_instances exists")
                serializer = WordSerializer(word_instances, many=True)
                return Response(serializer.data)

    return Response({'error': 'No entries found'}, status=404)
