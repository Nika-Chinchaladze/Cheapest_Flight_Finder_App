import requests
import os


class TequilaFinder:
    def __init__(self):
        self.location_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.my_header = {
            "apikey": os.environ.get("MY_KEY")
        }

    def get_iat_code(self, city):
        location_info = {
            "term": city,
            "location_types": "airport"
        }
        respond = requests.get(url=self.location_endpoint, params=location_info, headers=self.my_header)
        answer = respond.json()["locations"][0]["code"]
        return answer

    def get_flight_info(self, to_code, date_from, date_to, min_duration, max_duration, currency):
        flight_info = {
            "fly_from": "TBS",
            "fly_to": to_code,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": min_duration,
            "nights_in_dst_to": max_duration,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": currency
        }
        respond = requests.get(url=self.search_endpoint, params=flight_info, headers=self.my_header)
        answer = respond.json()["data"][0]
        price = answer["price"]
        city_from = answer["route"][0]["cityFrom"]
        iat_from = answer["route"][0]["cityCodeFrom"]
        city_to = answer["route"][0]["cityTo"]
        iat_to = answer["route"][0]["cityCodeTo"]
        start_date = answer["route"][0]["utc_departure"].split("T")[0]
        end_date = answer["route"][1]["utc_arrival"].split("T")[0]
        result = {
            "price": price,
            "city_from": city_from,
            "iat_from": iat_from,
            "city_to": city_to,
            "iat_to": iat_to,
            "start_date": start_date,
            "end_date": end_date
        }
        return result
