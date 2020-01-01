class Goods:
    def __init__(self, good_id, good_weight):
            self.id = good_id
            self.weight = good_weight



class Pallet:
    def __init__(self):
        self.load_time = {}
        self.unload_time = {}
    def load(self, object):




    def unload(self):


    def total_weight(self):
        total_weight = 0
        for id, pallet in self.pallets.items():
            if pallet.load_time and pallet.load_time <= t and (pallet.unload_time == None or pallet.unload_time > t):
                total_weight += pallet.weight

