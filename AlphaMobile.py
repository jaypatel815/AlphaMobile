from Location import Location
from Model import Model

# Factory locations for Smart4, Smart5, and Smart6
# Assembly of model to their specified factory
# Testing to see if it prints properly
class AlphaMobile:
    def __init__(self):
        # Set the manufacturing locations
        Singapore = Location("Singapore")
        NewYork = Location("New York")

        # Assembling the models
        Smart4 = Model()
        Smart5 = Model()
        Smart6 = Model()

        # Smart4 specifications
        Smart4.setLabel("Smart4")
        Smart4.setPrice("$400")

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

        # Assembly of Smart4 and Smart5 in Singapore
        Singapore4 = Singapore.assembleSmart(Smart4)
        # Print the location of the Singapore Factory
        print(Singapore)

        Singapore5 = Singapore.assembleSmart(Smart5)
        print(Singapore)

if __name__ == "__main__":
    # Test to see if it works
    AlphaMobile()
