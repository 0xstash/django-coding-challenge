from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView


@csrf_exempt
class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        return Response(data={}, status=200)
