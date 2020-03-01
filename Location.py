# Assembly of the models at the factory specified
class Location:
    def __init__(self, location = None, model = None):
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
        return "Factory Location: %s\nLabel: %s\nPrice: %s\n" %(self.location, self.model.label, self.model.price)
