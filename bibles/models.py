from django.conf import settings
from django.db import models
from django.utils import timezone


class Script(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class bibleList(models.Model):
    titles = ["ge", "exo", "lev", "num", "deu", "josh", "jdgs", "ruth", 
    "1sm", "2sm", "1ki", "2ki", "1chr", "2chr", "ezra", "neh", "est", "job",
    "psa", "prv", "eccl", "ssol", "isa", "jer", "lam", "eze", "dan", "hos",
    "joel", "amos", "obad", "jonah", "mic", "nahum", "hab", "zep", "hag",
    "zec", "mal", "mat", "mark", "luke", "john", "acts", "rom", "1cor", "2cor",
    "gal", "eph", "phi", "col", "1th", "2th", "1tim", "2tim", "titus", "phmn",
    "heb", "jas", "1pet", "2pet", "1jn", "2jn", "3jn", "jude", "rev"]
    titles_ko = ["창세기", "출애굽기", "레위기", "민수기", "신명기", "여호수아", 
    "사사기", "룻기", "사무엘상", "사무엘하", "열왕기상", "열왕기하", 
    "역대기상", "역대기하", "에스라", "느헤미야", "에스더", "욥기",
    "시편", "잠언", "전도서", "아가서", "이사야", "예레미야", "예레미야 애가", 
    "에스겔", "다니엘", "호세아", "요엘", "아모스", "오바댜", "요나", "미가",
    "나훔", "하박국", "스바냐", "학개", "스가랴", "말라기", "마태복음", "마가복음",
    "누가복음", "요한복음", "사도행전", "로마서", "고린도전서", "고린도후서",
    "갈라디아서", "에베소서", "빌립보서", "골로새서", "데살로니가전서", "데살로니가후서",
    "디모데전서", "디모데후서", "디도서", "빌레몬서", "히브리서", "야고보서",
    "베드로전서", "베드로후서", "요한일서", "요한이서", "요한삼서", "유다서", "요한계시록"]
    chapters_num =[50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 10,
    42, 150, 31, 12, 8, 66, 52, 5, 48, 12, 14, 3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4,
    28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22]