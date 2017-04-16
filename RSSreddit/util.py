import re
import requests
from xml.etree import ElementTree

# def urlbuilder():
#

def getXML(url):
    response = requests.get(url, headers={'User-agent': 'RSSreddit'})
    if response.status_code == 200:
        xmlelement = ElementTree.fromstring(response.content)
        return xmlelement

def tag_name(tag):
    return re.findall(r'}(\w+)', tag.tag)[0] or None

def recurseXML(element):
    data = {}
    for elem in element:
        item = tag_name(elem)
        if type(elem.text) is str:
            data[item] = elem.text
        elif elem.attrib:
            if item in data:
                data[item].append(elem.attrib)
            else:
                data[item] = [elem.attrib]
        else:
            if item in data:
                data[item].append(recurseXML(elem))
            else:
                data[item] = [recurseXML(elem)]
    return data
