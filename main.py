import datetime as dt
import re

from bs4 import BeautifulSoup
from urllib import request

STRFTIME = "%Y-%m-%d %H:%M"

def toDatetime(date_str):
    return dt.strptime(date_str, STRFTIME)

def findLastUpdate(soup):
    cur_update = soup.find("p", style="text-align: center;").text
    cur_update = re.sub(r".+(\d{4}.+) à (.+)", r"\1 \2", cur_update)
    return toDatetime(cur_update)

def initialParse(last_update, url):
    data = {}
    page = request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    cur_update = findLastUpdate(soup)
    if last_update == cur_update:
        data["last_update"] = last_update
        return data
    data["last_update"] = cur_update
    return data
