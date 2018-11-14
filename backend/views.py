from django.shortcuts import render, get_object_or_404
from backend.models import Country, State
from rest_framework import viewsets
from backend.serializers import CountrySerializer, StateSerializer


# Create your views here.
class CountryViewSet(viewsets.ModelViewSet):
    """API endpoint that allows countries to be viewed or edited."""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    """API endpoint that allows states to be viewed or edited."""
    queryset = State.objects.all()
    serializer_class = StateSerializer
    def get_queryset(self):
        countryCode = self.kwargs.get('code')
        country = get_object_or_404(Country, code=countryCode)
        return country.states.all()



    

