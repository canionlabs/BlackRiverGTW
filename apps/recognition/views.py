from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class RecFacesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({})
