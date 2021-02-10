from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    return render(request, "xmas/index.html", {"xmas": now.month==12 and now.day==25})