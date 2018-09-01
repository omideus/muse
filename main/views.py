from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import MuseumObject
from django.conf import settings

# Create your views here.


def getinfo(request, objnumber):
    detected_object = get_object_or_404(MuseumObject, ded_id=objnumber)
    return JsonResponse({
        'title': detected_object.title,
        'description': detected_object.description,
        'image': detected_object.image.url
    })
