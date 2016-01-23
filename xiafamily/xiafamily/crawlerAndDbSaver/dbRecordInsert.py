# -*- coding:utf-8 -*-
import codecs
from django.shortcuts import render
from familytree.models import familyMember as FM


def process():
    f = codecs.open("familyTree.txt", "r", "utf-8")
    num = 318
    for i in range(0, 318):
        id = f.readline()
        gender = f.readline()
        whatelse = f.readline()

        generation = ""
        name = ""
        match = ""
        spouse = ""

        try:
            generation, name, match, spouse = whatelse.split()
        except:
            generation, name = whatelse.split()
        # print id
        # print gender
        # print whatelse
        # print generation, name

        adminFM = FM(oldsystem_id=id, gender=gender, name=name, spouse_name=spouse)
        adminFM.save()
    f.close()

if __name__ == "__main__":
    process()