class Competition:
    name = ""
    country = ""
    technical_score = 0
    component_score = 0
    lost_score = 0

    def __init__(self, name, country, technical_score, component_score, lost_score):
        self.name = name
        self.country = country
        self.technical_score = float(technical_score)
        self.component_score = float(component_score)
        self.lost_score = float(lost_score)

    def __str__(self):
        return f"Név: {self.name}, ország: {self.country}, technikai pontszám: {str(self.technical_score)}, komponens pontszám: {str(self.component_score)}, levonás: {str(self.lost_score)} pont"
