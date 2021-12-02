# m_kreis.py

import math

class Kreis:

    __fields = ("Id", "Radius")
    __prototype = {"Id" : "Radius"}

    def __init__(self, **kwargs):

        for key in Kreis.__fields:
                if key in kwargs:
                    setattr(self, key, kwargs[key])
                else:
                    setattr(self, key, Kreis.__prototype[key]) # safety

    def umfang(self):
            return 2 * math.pi * self.Radius

    def flaeche(self):
        return 2 * math.pi * math.pi

    def __str__(self):
        return f'Id: {self.Id}\nRadius: {self.Radius}\nUmfang: {self.umfang()} \nFlaeche: {self.flaeche()}'
