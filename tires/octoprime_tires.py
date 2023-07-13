from .tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        sum = 0
        for i in range(len(self.wear)):
            sum+= self.wear[i]
        return sum >= 3
