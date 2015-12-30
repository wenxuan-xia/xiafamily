# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2


def getMainPage():
    url = "http://xiafamily.net/"
    html = urllib2.urlopen(url).read()
    BSobj = BeautifulSoup(html, "html.parser")
    list_group_item = BSobj.find_all("a", {"class": "list-group-item"})
    counter = 0

    f = open("familyTree.txt", "w")
    for item in list_group_item:
        gender = ""
        iss = item.find_all("i", {"class": "fa"})
        if "female" in str(iss[1]):
            gender = "female"
        else:
            gender = "male"
        counter += 1
        f.write("%d\n" %counter)
        f.write("%s\n" %gender)
        f.write(item.get_text().encode("utf-8"))
        # f.write("%s\n" %item["href"])
        # f.write(item["data-parent"])
        f.write("\n\n")

    f.close()


if __name__ == "__main__":
    getMainPage()
