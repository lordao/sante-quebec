from scraper import scrape
from models import Scrape, Region, Hospital, HospitalRecord


def last_scrape():
    model_select = (Scrape.select()
                    .order_by(Scrape.scrape_date.desc()))
    if not model_select.exists():
        return None
    return model_select.get().scrape_date


def main():
    last_update = last_scrape()
    print("Fetching page...")
    data = scrape("https://www.indexsante.ca/urgences/", last_update)
    cur_update = data.pop("last_update", last_update)
    if last_update == cur_update:
        print("Data already processed.")
        return
    all_records = []
    scrape_id = Scrape.create(scrape_date=cur_update).id
    defaults = {"scrape": scrape_id}
    for (region_str, records) in data.items():
        (region, _) = Region.get_or_create(nom=region_str, defaults=defaults)
        for record in records:
            hospital_name = record.pop("nom")
            (hospital, _) = Hospital.get_or_create(
                nom=hospital_name,
                region=region.id,
                defaults=defaults)
            record["hospital"] = hospital.id
            record["scrape"] = scrape_id
            all_records.append(record)
    HospitalRecord.insert_many(all_records).execute()
