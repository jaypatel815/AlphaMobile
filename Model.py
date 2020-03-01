# Create models
class Model:
    def __init__(self, label = None, price = 0):
        self.label = label
        self.price = price

    def getLabel(self):
        # Get the label of the model
        return self.label

    def getPrice(self):
        # Get the price of the model
        return self.price

    def setLabel(self, label):
        # Set the label of the model
        self.label = label

    def setPrice(self, price):
        # Set the price of the model
        self.price = price

    def __str__(self):
        # Return info about the model
        return "Label: %s\nPrice: %s" %(self.label, str(self.price))