import re
import time
import urllib.request

known_objects = set()


def parse():
    global known_objects
    census_link = "https://catagolue.appspot.com/census/b2n3s23-q/C1"
    response = urllib.request.urlopen(census_link)  # Getting HTML
    page_source = response.read().decode("utf-8")

    stuff = re.findall("<li>(.*?)</li>", page_source)
    for i in stuff:
        new_link = "https://catagolue.appspot.com/" + re.findall("\"(.*?)\"", i)[0]

        response = urllib.request.urlopen(new_link)  # Getting HTML
        page_source = response.read().decode("utf-8")

        objects = re.findall("<td><a href=\"(.*?)\">", page_source)
        for obj in objects:
            if obj.split("/")[2] not in known_objects:
                print("NEW OBJECT:", obj.split("/")[2])
            known_objects.add(obj.split("/")[2])


while True:
    parse()
    print("++++++++++++++++++++++++++++++")
    time.sleep(600)
