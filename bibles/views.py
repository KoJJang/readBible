from django.shortcuts import render

# Create your views here.
def bible_list(request):
    return render(request, 'bibles/bible_list.html', {})