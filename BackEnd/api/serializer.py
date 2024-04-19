from rest_framework import serializer
from .models import Persona 

class PersonaSerializer(serializer.ModelSerializer):
    class Meta:
        model=Persona
        fields = '__all__'