from django.http import HttpResponse
from django.shortcuts import render
import datetime
import json

info = '''[{
            "filename": "14 Too Long.m4a",
            "title": "Too Long",
            "duration": "10:00"
          },
          {
            "filename": "13 Face To Face.m4a",
            "title": "Face To Face",
            "duration": "04:00"
          },
          {
            "filename": "12 Short Circuit.m4a",
            "title": "Short Circuit",
            "duration": "03:26"
          },
          {
            "filename": "11 Veridis Quo.m4a",
            "title": "Veridis Quo",
            "duration": "05:44"
          }]'''

# Create your views here.
def hello(request):
   text = "Hello"
   return HttpResponse(text)


def date(request):
    today = datetime.datetime.now().date()
    return render(request, "hello.html", {"today": today})


def getSongsInfo(request):
    value = 1/0
    #return render(request, "songs.html", {"data": json.loads(info)})
    return HttpResponse(info)