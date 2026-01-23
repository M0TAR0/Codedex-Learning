# This is a Python code for a Pokédex

class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry #Int number
        self.name = name #Str
        self.types = types #Str
        self.description = description #str
        self.is_caught = is_caught #bool
    
    def speak(self):
        print(self.name, self.name + "!\n")

    def display_details(self):
        print("Entry Number:", self.entry)
        print("Name:", self.name)
        print("Type:", self.types)
        print("Description:", self.description )
        if self.is_caught:
            print(f"{self.name} has already been caught!\n")
        else:
            print(f"{self.name} has not been caught!\n")
            

charmander = Pokemon(4, "Charmander", "Fire", "The flame on its tail shows the strength of its life-force. If Charmander is weak, the falme also burns weakly.", True)
Tatsugiri = Pokemon(978, "Tatsugiri", "Dragon, Water", "Tatsugiri will battle furiously among themselves to determine which of them will get to partner with a particular Dondozo.", False)
pecharunt = Pokemon(1025, "Pecharunt", "Poison, Ghost", "It feeds others toxic mochi that draw out desires and capabilities. Those who eat the mochi fall under Pecharunt’s control, chained to its will.", True)

charmander.speak()
Tatsugiri.display_details()
pecharunt.display_details()