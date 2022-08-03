from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


places = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [37.62, 55.793676]
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
                "coordinates": [37.64, 55.753676]
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