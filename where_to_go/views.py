from django.http import Http404
from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404, render
from django.urls import reverse
from places.models import Image, Place


def get_place_details(request, place_id):
    try:
        place = Place.objects.get(pk=place_id)
    except Place.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    images = get_list_or_404(Image, place=place)
    place_json = {
        "title": place.title,
        'imgs': [item.image.url for item in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }
    return JsonResponse(place_json,
                        safe=False,
                        json_dumps_params={
                            'ensure_ascii': False})


def index(request):
    places = Place.objects.all()

    places_with_description = []
    for place in places:
        description = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.longitude,
                                        place.latitude]
                    },
                    "properties": {
                        "title": place.title,
                        "placeId": place.id,
                        "detailsUrl": reverse(get_place_details, args=[place.id])
                    }
                }
            ]
        }
        places_with_description.append(description)
    return render(request,
                  'index.html',
                  {'places_geojson': places_with_description})
