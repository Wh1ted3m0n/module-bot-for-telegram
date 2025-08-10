from core.parcers import habr_par,opennet_par

class Parcer:
    def __init__(self):
        self.habrP = habr_par.parcer_habr()
        self.opennetP = opennet_par.openNet_parcer()
