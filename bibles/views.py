from django.shortcuts import render
from .models import Script
from django.utils import timezone

# Create your views here.
def bible_list(request):
    bibles = Script.objects.order_by('published_date')
    return render(request, 'bibles/bible_list.html', {'bibles': bibles})