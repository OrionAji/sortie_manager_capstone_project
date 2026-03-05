from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .models import Aircraft, Pilot, Sortie
from .serializers import AircraftSerializer, PilotSerializer, SortieSerializer

class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer

class PilotViewSet(viewsets.ModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer

class SortieViewSet(viewsets.ModelViewSet):
    queryset = Sortie.objects.all()
    serializer_class = SortieSerializer

    # Criterion 8: Custom Error Handling for our "Blocking" logic
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            # Returns 400 Bad Request if Aircraft is grounded or Pilot isn't rested
            return Response(
                {"error": "Mission Validation Failed", "details": e.messages},
                status=status.HTTP_400_BAD_REQUEST
            )