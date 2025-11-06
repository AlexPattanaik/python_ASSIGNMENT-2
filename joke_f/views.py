
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Joke
from .serializers import Jokeserializers
import requests

# Create your views here.
@api_view(["GET"])
def fetch_and_store_jokes(request):
    joke_added=0
    for i in range (10):
        url="https://v2.jokeapi.dev/joke/any?amount=10"
        response=requests.get(url)
        data=response.json()
        if 'jokes' not in data:
            return Response({"error":"failed to Fetch jokes."},status=500)
        joke_to_create=[]
        for j in data["jokes"]:
            joke_type=j.get("type")
            if joke_type =='single':
                joke_text=j.get('joke')
                setup=None
                delivery=None
            else:
                joke_text = None
                setup = j.get("setup")
                delivery = j.get("delivery")
            joke_to_create.append(Joke(category=j.get('category'),
                                       type=joke_type,
                                       joke=joke_text,
                                       setup=setup,
                                       delivery=delivery,
                                       nsfw=j.get("flags",{}).get("nsfw",False),
                                       political=j.get("flags",{}).get("political",False),
                                       sexist=j.get("flags",{}).get("sexist",False),
                                       safe=j.get("safe",True),
                                       lang=j.get("lang","en")
            ))
        Joke.objects.bulk_create(joke_to_create,ignore_conflicts=True)
        joke_added+=len(joke_to_create)
        #return Response({"message": f"{len(joke_to_create)} jokes has stored successfully"})
    return Response({"message": f"{joke_added} jokes has stored successfully"})



@api_view(["GET"])
def get_jokes(request):
    limit = int(request.GET.get("limit",1))
    jokes = Joke.objects.all()[:limit]
    serializer= Jokeserializers(jokes,many=True)
    return  Response(serializer.data)

