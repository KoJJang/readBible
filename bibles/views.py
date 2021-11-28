from django.shortcuts import get_object_or_404, render

# from readBible import bibles
from .models import Script
from django.utils import timezone

# Create your views here.
def bible_list(request):
    bibles = Script.objects.order_by('published_date')
    return render(request, 'bibles/bible_list.html', {'bibles': bibles})

def bible_detail(request, pk):
    bible = get_object_or_404(Script, pk=pk)
    return render(request, 'bibles/bible_detail.html', {'bible': bible})