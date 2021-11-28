from django.shortcuts import get_object_or_404, render, redirect

# from readBible import bibles
from .models import Script
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def bible_list(request):
    bibles = Script.objects.order_by('published_date')
    return render(request, 'bibles/bible_list.html', {'bibles': bibles})

def bible_detail(request, pk):
    bible = get_object_or_404(Script, pk=pk)
    return render(request, 'bibles/bible_detail.html', {'bible': bible})

def bible_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            bible = form.save(commit=False)
            bible.author = request.user
            bible.pubilshed_date = timezone.now()
            bible.save()
            return redirect('bible_detail', pk=bible.pk)
    else:
        form = PostForm()
    return render(request, 'bibles/bible_edit.html', {'form': form})

def bible_edit(request, pk):
    bible = get_object_or_404(Script, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=bible)
        if form.is_valid():
            bible = form.save(commit=False)
            bible.author = request.user
            bible.published_date = timezone.now()
            bible.save()
            return redirect('bible_detail', pk=bible.pk)
    else:
        form = PostForm(instance=bible)
    return render(request, 'bibles/bible_edit.html', {'form': form})