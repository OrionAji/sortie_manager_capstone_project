from django.shortcuts import render
import logging  # 1. Add this import

logger = logging.getLogger('sorties')  # 2. Add this initialization
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .models import Aircraft, Pilot, Sortie
from .serializers import AircraftSerializer, PilotSerializer, SortieSerializer

from rest_framework import filters # Add this import
from django_filters.rest_framework import DjangoFilterBackend # Add this import

class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    
    # Adding Filter and Search capabilities
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['tail_number']

    # Keep your readiness_report action here too...
    
class PilotViewSet(viewsets.ModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['rank']
    search_fields = ['callsign']

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

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            # Criterion 8: Log the blocked attempt for safety audits
            logger.warning(f"BLOCKED SORTIE: {request.user} attempted to schedule mission. Error: {e.messages}")
            
            return Response(
                {"error": "Mission Validation Failed", "details": e.messages},
                status=status.HTTP_400_BAD_REQUEST
            )