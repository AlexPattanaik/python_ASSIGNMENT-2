from .models import Joke
from rest_framework import serializers
class Jokeserializers(serializers.ModelSerializer):
    class Meta:
        model=Joke
        fields='__all__'