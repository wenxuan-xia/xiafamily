from django.shortcuts import render
from django.http import HttpResponse

from .models import familyMember as fm
# Create your views here.


def index(request):
    member = fm.objects.all()
    return render(request, 'index.html', {'member' : member} )
