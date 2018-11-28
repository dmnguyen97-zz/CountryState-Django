from backend.models import Country, State
from django.shortcuts import get_object_or_404
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'code', 'name')

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'code', 'name', 'country_id')

class CreateStateSerializer(serializers.ModelSerializer):
    country_code = serializers.CharField(source='country_id.code')

    class Meta:
        model = State
        fields = ('code', 'name', 'country_code')

    def create(self, validated_data):
        print ('\n\n\n\n\nValidated_Data:' + str(validated_data) + '\n\n\n\n\n')
        country_object = validated_data.pop('country_id')
        country = country_object.pop('code')
        country = get_object_or_404(Country, code=country)
        state = State.objects.create(**validated_data, country_id=country)
        return state


