# -*- coding:utf-8 -*-
import codecs
from django.shortcuts import render
from familytree.models import familyMember as FM


def process():
    gen_recorder = [0] * 10
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
        belongs = 0
        try:
            generation, name, match, spouse = whatelse.split()
            belongs = gen_recorder[int(generation) - 1]
            gen_recorder[int(generation)] = i + 1
        except:
            generation, name = whatelse.split()
            belongs = gen_recorder[int(generation) - 1]
            gen_recorder[int(generation)] = i + 1
        # print gen_recorder\
        # print id
        # print gender
        # print whatelse
        # print generation, name

        adminFM = FM(oldsystem_id=id, gender=gender, name=name, spouse_name=spouse, generation=generation, belongs_to = belongs)
        adminFM.save()
    f.close()

if __name__ == "__main__":
    process()
