from random import randint, choice

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


LOWER_CHARS = [chr(i) for i in range(97, 123)]
UPPER_CHARS = [chr(i) for i in range(65, 91)]
DIGITS = [i for i in range(10)]
SPECIAL_CHARS = ['%', '_', '-', '!', '$', '&', '#', '=', '@']


@api_view(['GET'])
def generate(request):
    lower    = request.GET.get('lower', "true").lower() == "true"
    upper    = request.GET.get('upper', "true").lower() == "true"
    digits   = request.GET.get('digits', "true").lower() == "true"
    special  = request.GET.get('special', "true").lower() == "true"
    length   = int(request.GET.get('length', 16))
    elements = dict()
    password = ""
    key = 0

    if lower:
        elements[key] = LOWER_CHARS
        key += 1
    if upper:
        elements[key] = UPPER_CHARS
        key += 1
    if digits:
        elements[key] = DIGITS
        key += 1
    if special:
        elements[key] = SPECIAL_CHARS
        key += 1

    for i in range(length):
        char_type = randint(0, key-1)
        password += str(choice(elements[char_type]))

    return Response({"password": password}, status=status.HTTP_200_OK)