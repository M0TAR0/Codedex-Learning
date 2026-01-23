class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

Guanajuato = City("Guanajuato", "Mexico", 40000, ["Monumento al Pipilf", "El Teatro Juárez"])
CDMX = City("Ciudad de México", "México", 5000000, ["Chapultepec", "El Palacio de Bellas Artes", "Museo Memoria y Tolerancia"])

print(vars(Guanajuato))
print(vars(CDMX))
