from engine.foodpanda import *

def test_fetch_items():
    panda = FoodPandaScraping()
    res = panda.fetch_items(lat=35.5308325, lng=139.7029125)
    print(len(res))
    print(res[0].__dict__)