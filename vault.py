class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self): 
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

# Creating instances of Vault
potter = Vault(100, 50, 25)
print(potter)  # Output: 100 Galleons, 50 Sickles, 25 Knuts

weasley = Vault(25, 50, 100)
print(weasley)  # Output: 25 Galleons, 50 Sickles, 100 Knuts

# Adding two Vault instances
total = potter + weasley
print(total)  # Output: 125 Galleons, 100 Sickles, 125 Knuts
