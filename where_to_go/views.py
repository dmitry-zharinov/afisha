from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from places.models import Place


def get_place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = place.images.all()
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
                        "detailsUrl": reverse(get_place_details,
                                              args=[place.id])
                    }
                }
            ]
        }
        places_with_description.append(description)
    return render(request,
                  'index.html',
                  {'places_geojson': places_with_description})
