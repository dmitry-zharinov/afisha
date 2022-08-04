from django.http import Http404
from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404, render
from places.models import Image, Place

moscow_legends = Place.objects.get(placeId='moscow_legends')
roofs24 = Place.objects.get(placeId='roofs24')

places_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [moscow_legends.longitude,
                                moscow_legends.latitude]
            },
            "properties": {
                "title": "«Легенды Москвы",
                "placeId": "moscow_legends",
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [roofs24.longitude,
                                roofs24.latitude]
            },
            "properties": {
                "title": "Крыши24.рф",
                "placeId": "roofs24",
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json"
            }
        }
    ]
}


def show_start_page(request):
    return render(request,
                  'index.html',
                  {'places_geojson': places_geojson})


def get_place_json(place):
    images = get_list_or_404(Image, place=place)
    place_json = {
        "title": place.title,
        'img': [item.image.url for item in images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }
    return place_json


def places(request, post_id):
    try:
        place = Place.objects.get(pk=post_id)
    except Place.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    return JsonResponse(get_place_json(place), safe=False,
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})
