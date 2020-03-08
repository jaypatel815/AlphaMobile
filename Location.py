# Assembly of the models at the factory specified
from Model import Model


class Location:
    def __init__(self, location=None, model=None):
        self.location = location
        self.model = model

    def assembleSmart(self, model):
        # Set the model for the factory
        self.model = model
        return self.model

    def getLocation(self):
        # Return factory location
        return self.location

    def getModel(self):
        # Return model
        return self.model

    def setPrice(self, price):
        # Set the price of the model
        self.model.setPrice(price)

    def setLabel(self, label):
        # Set label for model
        self.model.setLabel(label)

    def __str__(self):
        # Return info about the models and location
        return "Factory Location: %s\nLabel: %s\nPrice: %s\n" % (self.location, self.model.label, self.model.price)


class Singapore():
    def __init__(self):
        Singapore = Location("Singapore")

        Smart4 = Model()
        Smart5 = Model()

        # Smart4 specifications
        Smart4.setLabel("Smart4")
        Smart4.setPrice("$400")

        # Smart5 specifications
        Smart5.setLabel("Smart5")
        Smart5.setPrice("$599.99")

        # Assembly of Smart4 and Smart5 in Singapore
        Singapore4 = Singapore.assembleSmart(Smart4)
        # Print the location of the Singapore Factory
        print(Singapore)

        Singapore5 = Singapore.assembleSmart(Smart5)
        print(Singapore)


class NewYork():
    def __init__(self):
        NewYork = Location("New York")

        Smart5 = Model()
        Smart6 = Model()

        # Smart5 specifications
        Smart5.setLabel("Smart5")
        Smart5.setPrice("$599.99")

        # Smart6 specifications
        Smart6.setLabel("Smart6")
        Smart6.setPrice("$1099.99")

        # Assembly of Smart5 and Smart6 in New York
        NewYork5 = NewYork.assembleSmart(Smart5)
        # Print the location of the New York Factory
        print(NewYork)

        NewYork6 = NewYork.assembleSmart(Smart6)
        print(NewYork)


if __name__ == "__main__":
    # Test to see if it works
    Singapore()
    NewYork()
