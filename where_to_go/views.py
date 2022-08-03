from django.shortcuts import render
from places.models import Place

moscow_legends = Place.objects.get(placeId='moscow_legends')
roofs24 = Place.objects.get(placeId='roofs24')

places = {
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
                  {'places_geojson': places})