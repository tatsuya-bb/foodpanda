
class Item():

    def __init__(
        self, name: str=None, address: str=None, post_code: str=None, review_rate: float=None, review_number: int=None,
        url: str=None, vendor_points: int=None, minimum_delivery_fee: int=None, latitude: float=None, longitude: float=None,
        cuisines: str=None, website: str=None 
        ):
        self.name = name
        self.address = address
        self.post_code = post_code
        self.review_rate = review_rate
        self.review_number = review_number
        self.url = url
        self.vendor_points = vendor_points
        self.minimum_delivery_fee = minimum_delivery_fee
        self.latitude = latitude
        self.longitude = longitude
        self.cuisines = cuisines
        self.website = website


    def to_dict(self):
        return self.__dict__.copy()