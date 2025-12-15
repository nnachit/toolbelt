from secrets import choice, randbelow

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


LOWER_CHARS = [chr(i) for i in range(97, 123)]
UPPER_CHARS = [chr(i) for i in range(65, 91)]
DIGITS = [str(i) for i in range(10)]
SPECIAL_CHARS = ['%', '_', '-', '!', '$', '&', '#', '=', '@']

MIN_LENGTH = 4
MAX_LENGTH = 128


@api_view(['GET'])
def generate(request):
    lower = request.GET.get('lower', "true").lower() == "true"
    upper = request.GET.get('upper', "true").lower() == "true"
    digits = request.GET.get('digits', "true").lower() == "true"
    special = request.GET.get('special', "true").lower() == "true"

    try:
        length = int(request.GET.get('length', 16))
    except ValueError:
        return Response(
            {"error": "length must be an integer"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if not MIN_LENGTH <= length <= MAX_LENGTH:
        return Response(
            {"error": f"length must be between {MIN_LENGTH} and {MAX_LENGTH}"},
            status=status.HTTP_400_BAD_REQUEST
        )

    char_pools = []
    if lower:
        char_pools.append(LOWER_CHARS)
    if upper:
        char_pools.append(UPPER_CHARS)
    if digits:
        char_pools.append(DIGITS)
    if special:
        char_pools.append(SPECIAL_CHARS)

    if not char_pools:
        return Response(
            {"error": "At least one character type must be selected"},
            status=status.HTTP_400_BAD_REQUEST
        )

    password = ""
    for _ in range(length):
        pool = char_pools[randbelow(len(char_pools))]
        password += choice(pool)

    return Response({"password": password}, status=status.HTTP_200_OK)