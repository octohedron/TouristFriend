
class Business:
    def __init__(self, name, address, rating, rating_count, location):
        self.name = name
        self.address = address
        self.rating = rating
        self.rating_count = rating_count
        self.bayesian = 0.0
        self.source_count = 1
        self.location = location
