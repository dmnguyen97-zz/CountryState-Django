from django.shortcuts import render, get_object_or_404
from backend.models import Country, State
from rest_framework import viewsets
from backend.serializers import CountrySerializer, StateSerializer, CreateStateSerializer


# Create your views here.
class CountryViewSet(viewsets.ModelViewSet):
    """API endpoint that allows countries to be viewed or edited."""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def list(self, request):
        countrydata = super().list(self, request)
        countrydata.data = countrydata.data['results']
        return countrydata

class StateViewSet(viewsets.ModelViewSet):
    """API endpoint that allows states to be viewed or edited."""
    queryset = State.objects.all()

    def get_queryset(self):
        countryCode = self.kwargs.get('code')
        country = get_object_or_404(Country, code=countryCode)
        return country.states.all()
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'GET':
            serializer_class = StateSerializer
        elif self.request.method == 'POST':
            serializer_class = CreateStateSerializer
        return serializer_class
    
    def list(self, request, **kwargs):
        statedata = super().list(self, request, **kwargs)
        statedata.data = statedata.data['results']
        return statedata



    

