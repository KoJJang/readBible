from django.shortcuts import get_object_or_404, render, redirect

# from readBible import bibles
from .models import Script, bibleList
from django.utils import timezone
from .forms import PostForm
import requests
import json
import sqlite3

# Create your views here.
def bible_list(request):#TODO:: verse 선택 시 select의 verse 수정
    if request.method == "POST":
        print(request.POST)
        selected_title = request.POST.get("title")
        selected_chapter = request.POST.get("chapter")
        start_verse = request.POST.get("start_verse")
        end_verse = request.POST.get("end_verse")
        context = {
            'all_title': bibleList.titles_ko,
            'selected_title': selected_title,
            'selected_chapter': selected_chapter,
            'start_verse': start_verse,
            'end_verse': end_verse,
            'all_chapter': range(1,bibleList.chapters_num[int(selected_title)-1]+1),
        }
        if start_verse == "1" and end_verse == "1":
            isVerseSelected = False
        else:
            isVerseSelected = True
    else:
        selected_title = 1
        selected_chapter = 1
        context = {
            'all_title': bibleList.titles_ko,
            'all_chapter': range(1,bibleList.chapters_num[0]+1),
            'selected_chapter': 1,
            'start_verse': 1,
            'end_verse':1,
            'tmp': bibleList.titles_ko
        }
        isVerseSelected = False
    con = sqlite3.connect('bible2.db')
    cur = con.cursor()
    
    cmd = 'SELECT * FROM bible2 where long_label=="'+ bibleList.titles_ko[int(selected_title)-1] +'" AND chapter=='+ str(selected_chapter) +' AND paragraph>=1 AND paragraph<=300'
    whe = []
    all_verse = 1
    for row in cur.execute(cmd):
        whe.append(str(row[5]))
        all_verse += 1
    if isVerseSelected:
        whe = []
        cmd = 'SELECT * FROM bible2 where long_label=="'+ bibleList.titles_ko[int(selected_title)-1] +'" AND chapter=='+ str(selected_chapter) +' AND paragraph>='+start_verse+' AND paragraph<='+end_verse
        for row in cur.execute(cmd):
            whe.append(str(row[5]))
    context['whe'] = whe
    context['all_verse'] = range(1,all_verse)
    con.close()
    return render(request, 'bibles/bible_list.html', context)

def bible_detail(request, pk):
    bible = get_object_or_404(Script, pk=pk)
    return render(request, 'bibles/bible_detail.html', {'bible': bible})

def bible_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            bible = form.save(commit=False)
            bible.author = request.user
            # bible.pubilshed_date = timezone.now()
            bible.save()
            return redirect('bible_detail', pk=bible.pk)
    else:
        form = PostForm()
    # con = sqlite3.connect('bible2.db')
    # cur = con.cursor()
    whe = []
    # for row in cur.execute('SELECT script FROM bible where chap=="ge" AND chap_num==1 AND verse_num>=1 AND verse_num<=100'):
    #     whe = whe + str(row) + '\n'
    return render(request, 'bibles/bible_edit.html', {'form': form, 'whe': whe})

def bible_edit(request, pk):
    bible = get_object_or_404(Script, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=bible)
        if form.is_valid():
            bible = form.save(commit=False)
            bible.author = request.user
            bible.text = requests.get('http://ibibles.net/quote.php?kor-mat/5:3-300')
            print(bible.text)
            # bible.published_date = timezone.now()
            bible.save()
            return redirect('bible_detail', pk=bible.pk)
    else:
        form = PostForm(instance=bible)
    whe="zzzz"
    return render(request, 'bibles/bible_edit.html', {'form': form, 'whe': whe})
