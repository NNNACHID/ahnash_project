class Snake:

    def __init__(self, family, genus, species, subspecies, averagelength, area, optimaltemp):
        self.family = family
        self.genus = genus
        self.species = species
        self.subspecies = subspecies
        self.averagelength = averagelength
        self.area = area
        self.optimaltemp = optimaltemp

    def __str__(self):
            return f'family: {self.family}' \
                   f'genus: {self.genus}' \
                   f'species: {self.species}' \
                   f'subspecies: {self.subspecies}' \
                   f'averagelength: {self.averagelength}' \
                   f'area: {self.area}' \
                   f'optimaltemp: {self.optimaltemp}'