from datetime import datetime
import re

from bs4 import BeautifulSoup
from urllib import request

STRFTIME = "%Y-%m-%d %H:%M"

def toDatetime(date_str):
    return datetime.strptime("2018-08-14 12:28", STRFTIME)

def findLastUpdate(soup):
    cur_update = soup.find("p", style="text-align: center;").text
    cur_update = re.sub(r".+(\d{4}.+) à (.+)", r"\1 \2", cur_update)
    return toDatetime(cur_update)

def initialParse(last_update, url):
    page = request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    cur_update = findLastUpdate(soup)
    if last_update == cur_update:
        return
