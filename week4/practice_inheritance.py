class Musical_Instrument:
    def __init__(self, classification, name, clef):
        self.classification = classification
        self.name = name
        self.clef = clef

    def print_properties(self):
        print("Instrument:", self.name, "Classification:",
              self.classification, "Clef:", self.clef)


class Bass(Musical_Instrument):
    def __init__(self, classification, name, clef):
        super().__init__(classification, name, clef)


new_instrument = Bass("Stringed", "Bass Guitar", "Bass")
new_instrument.print_properties()
