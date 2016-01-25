# -*- coding: utf-8 -*-

from familytree.models import familyMember as fm

def default_change():
    obj = fm.objects.all()
    for person in obj:
        # print person.gender
        if "female" in person.gender:
            person.gender = "女"
        elif "male" in person.gender:
            person.gender = "男"
        person.save()
    print obj


def find_house():
    obj = fm.objects.all()
    mystr = "未知"
    mystr = mystr.decode("utf-8")
    for person in obj:
        if mystr in person.house:
            # find belonging
            bls2 = person.belongs_to
            fa = fm.objects.filter(oldsystem_id=bls2)[0]
            if mystr not in fa.house:
                person.house = fa.house
                # print fa.house
                person.save()



if __name__ == "__main__":
    # default_change()
    # find_house()
    
