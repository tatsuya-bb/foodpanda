import os
import sys
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from engine.foodpanda import *
from common.utility import *

def crawle():
    panda = FoodPandaScraping()
    items = panda.fetch_items(lat=35.5308325, lng=139.7029125)

    df = class_list_to_df(items)
    df.to_excel("store_list.xlsx")


crawle()