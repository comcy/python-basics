# m_person.py


class Person:

    __fields = ("Vorname", "Nachname", "Groesse", "Gewicht")
    __prototype = {"Vorname" : "Max", "Nachname" : "Mustermann"}

    # Konstruktor: new / init
    # Magic Methods __yyy__(self, ...)
    # def __init__(self, vn ="", nn="", gr=0, ge=0):
    # def __init__(self, **kwargs):


    def __init__(self, **kwargs):

        # for key in kwargs:
        #     if key in Person.__fields:
        #         setattr(self,key,kwargs[key])

        for key in Person.__fields:
                if key in kwargs:
                    setattr(self, key, kwargs[key])
                else:
                    setattr(self, key, Person.__prototype[key]) # safety


    def __setattr__(self, name, value):
        print("NEU", name, value)

        if name in Person.__fields:
            return super().__setattr__(name, value)
        else: 
            raise Exception("FELD UNBEKANNT: " + name)
            # print("EROOOOOOR")

    # def __init__(self, vn, nn, groesse, gewicht):

    #     self.Vorname = vn
    #     self.Nachname = nn
    #     self.Groesse = groesse
    #     self.Gewicht = gewicht
        
    #     print(self, type(self))



    def bmi(self):
        return self.Gewicht/(self.Groesse/100)**2


    def abnehmen(self, val):
        self.Gewicht -= val

    def __str__(self):
        return f'{self.Vorname};{self.Nachname};{self.Gewicht};{self.Groesse};{self.bmi()}'

    def __int__(self):
        return 42
