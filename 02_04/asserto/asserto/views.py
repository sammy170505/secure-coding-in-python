from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):
    try:
        assert request.user.is_authenticated
        return Response({'success': True}, status=status.HTTP_200_OK)
    except AssertionError:
        return Response({'success': False}, status=status.HTTP_403_FORBIDDEN)

