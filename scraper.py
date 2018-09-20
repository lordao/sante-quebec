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


def getCities(soup):
    return [city for city in soup.findAll("h2")]


def getUrgenceTables(citiesSoup):
    urgentClass = {"class": "urgences"}
    return [city.findNext("table", attrs=urgentClass) for city in citiesSoup]


def getInstallations(uTablesSoup):
    return [
        [scrapeInstallation(row.findChildren("td"))
         for row in table.findChildren("tr")[1:]]
        for table in uTablesSoup
    ]


def scrapeInstallation(cols):
    data = [col.text for col in cols]
    installation = {
        "nom": data[0],
        "civieres_fonctionnelles": int(data[1]),
        "civieres_occupees": int(data[2]),
        "taux_occupation": float("0." + data[3][:-1]),
        "patients_plus_24": int(data[4]),
        "patients_plus_48": int(data[5])
    }
    return installation


def scrapePage(soup):
    cities = getCities(soup)
    tables = getUrgenceTables(cities)
    installations = getInstallations(tables)
    citiesNames = [city.text for city in cities]
    return dict(zip(citiesNames, installations))


def scrape(url, last_update=None):
    soup = getSoup(url)
    cur_update = findLastUpdate(soup)
    if last_update == cur_update:
        return {"last_update": last_update}
    data = scrapePage(soup)
    data["last_update"] = cur_update
    return data
