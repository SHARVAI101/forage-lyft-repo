from .tires import Tires

class CarriganTires(Tires):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        for i in range(len(self.wear)):
            if self.wear[i] >= 0.9:
                return True
        return False
