from django.shortcuts import render
from django.http import HttpResponse

from .models import familyMember as fm
# Create your views here.


def index(request):
    a = fm.objects.all()
    print a
    return render(request, 'index.html', {} )
