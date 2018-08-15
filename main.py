from datetime import datetime
import re

from bs4 import BeautifulSoup
from urllib import request

STRFTIME = "%Y-%m-%d %H:%M"

def toDatetime(date_str):
    return datetime.strptime(date_str, STRFTIME)

def findLastUpdate(soup):
    cur_update = soup.find("p", style="text-align: center;").text
    cur_update = re.sub(r".+(\d{4}.+) à (.+)", r"\1 \2", cur_update)
    return toDatetime(cur_update)

def getSoup(url):
    page = request.urlopen(url)
    return BeautifulSoup(page, "html.parser")

def initialParse(last_update, url):
    data = {}
    soup = getSoup(url)
    cur_update = findLastUpdate(soup)
    if last_update == cur_update:
        data["last_update"] = last_update
        return data
    data["last_update"] = cur_update
    return data
