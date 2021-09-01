import time
import re
import json
from pprint import pprint

from common.selenium_manager import SeleniumManager
from models.item import Item
from common.logger import set_logger
from common.utility import *

logger = set_logger(__name__)

FOODPANDA_SEARCH_URL = "https://www.foodpanda.co.jp/restaurants/new?lat={lat}&lng={lng}&vertical=restaurants"

class FoodPandaScraping():

    def __init__(self):
        self.manager = SeleniumManager(use_headless=False)
        self.manager.start_chrome()


    def fetch_item(self, url: str):
        self.manager.chrome.get(url)
        item_dict = self.manager.chrome.execute_script("return window.runParams")
        item = self._extract_item_dict(item_dict)
        print(item.to_dict())
        # pprint(item)
        # with open("item_data_test.json", mode="w", encoding="utf-8_sig") as f:
        #     f.write(json.dumps(item, ensure_ascii=False))


    def _extract_item_dict(self, item_dict: dict):
        data = item_dict.get("data")
        if not data:
            logger.error("data not found")
            return None
        max_price = int(data["priceModule"]["maxActivityAmount"]["value"] * self.currency_rate)
        min_price = int(data["priceModule"]["minActivityAmount"]["value"] * self.currency_rate)
        try:
            return LocalAliexpressItem(
                name=data["titleModule"]["subject"], 
                description="", 
                max_price=max_price, 
                min_price=min_price,
                image_urls=[], specs=[], stock=0, url="",product_id="",
                average_star=0.0, trade_count=0
            )
        except Exception as e:
            logger.error(e)
            return None

    
    def fetch_items(self, lat: float, lng: float, page_limit: int=10):
        items = []
        self.manager.chrome.get(FOODPANDA_SEARCH_URL.format(lat=lat, lng=lng))
        items_dict = self.manager.chrome.execute_script("return window.__PRELOADED_STATE__")
        
        items = []
        for store in items_dict["organicList"]["vendors"]:
            try:
                items.append(
                    Item(
                        address = store["address"] + (( " " + store["address_line2"]) if store["address_line2"] else ""),
                        name = store["name"],
                        url = store["redirection_url"],
                        post_code = store["post_code"],
                        review_number = store["review_number"],
                        review_rate = store["rating"],
                        vendor_points = store["vendor_points"],
                        website = store["website"],
                        latitude = store["latitude"],
                        longitude = store["longitude"],
                        cuisines = ",".join([cuisine["name"] for cuisine in store["characteristics"]["cuisines"]]),
                        minimum_delivery_fee = store["minimum_delivery_fee"]
                    )
                )
            except Exception as e:
                logger.error(f"fetch item dict error:{e}")
                break
        return items