from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from .models import familyMember as fm


def getWholeFamilyMembers(request):
    member = fm.objects.all()
    # print json.dumps(member)
    rst = []
    for person in member:
        pers = {}
        pers['name'] = person.name
        pers['house'] = person.house
        pers['generation'] = person.generation
        pers['belongs_to'] = person.belongs_to
        pers['oldsystem_id'] = person.oldsystem_id
        pers['gender'] = person.gender
        pers['married'] = person.married
        pers['spouse_name'] = person.spouse_name
        pers['location'] = person.location
        pers['education'] = person.education
        pers['careers'] = person.careers
        pers['links'] = person.links
        rst.append(pers)

    return HttpResponse(json.dumps(rst))
