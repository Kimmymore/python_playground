class DogBreed:
  def __init__(self, name, description, temperament, origin):
    self.name = name
    self.description = description
    self.temperament = temperament
    self.origin = origin

  def get_info(self):
    info = f"Name: {self.name}\n"
    info += f"Description: {self.description}\n"
    info += f"Temperament: {self.temperament}\n"
    info += f"Origin: {self.origin}\n"
    return info

# Create instances of dog breeds
australian_shepherd = DogBreed("Australian Shepherd", "Medium", "Intelligent, Energetic, Work-Oriented", "United States")
beagle = DogBreed("Beagle", "Small", "Curious, Merry, Friendly", "England")
boxer = DogBreed("Boxer", "Large", "Playful, Energetic, Friendly", "Germany")
bulldog = DogBreed("Bulldog", "Medium", "Docile, Willful, Friendly", "England")
chihuahua = DogBreed("Chihuahua", "Small", "Graceful, Charming, Sassy", "Mexico")
dachshund = DogBreed("Dachshund", "Small", "Clever, Stubborn, Devoted", "Germany")
golden_retriever = DogBreed("Golden Retriever", "Large", "Intelligent, Friendly, Devoted", "Scotland")
great_dane = DogBreed("Great Dane", "Extra Large", "Friendly, Patient, Dependable", "Germany")
king_charles_spaniel = DogBreed("King Charles Spaniel", "Small", "Affectionate, Gentle, Graceful", "United Kingdom")
labradoodle = DogBreed("Labradoodle", "Medium", "Intelligent, Friendly, Outgoing", "Australia")
labrador_retriever = DogBreed("Labrador Retriever", "Large", "Outgoing, Even Tempered, Gentle", "Canada")
pembroke_welsh_corgi = DogBreed("Pembroke Welsh Corgi", "Small", "Smart, Alert, Affectionate", "Wales")
pomeranian = DogBreed("Pomeranian", "Small", "Extroverted, Friendly, Intelligent", "Germany")
shih_tzu = DogBreed("Shih Tzu", "Small", "Affectionate, Outgoing, Playful", "China")
siberian_husky = DogBreed("Siberian Husky", "Large", "Outgoing, Alert, Gentle", "Russia")
toy_poodle = DogBreed("Toy Poodle", "Small", "Intelligent, Alert, Active", "France")


# Example usage
print(australian_shepherd.get_info())
print(beagle.get_info())
print(boxer.get_info())
print(bulldog.get_info())
print(chihuahua.get_info())
print(dachshund.get_info()
print(golden_retriever.get_info())
print(great_dane.get_info())
print(king_charles_spaniel.get_info())
print(labradoodle.get_info())
print(labrador_retriever.get_info())
print(pembroke_welsh_corgi.get_info())
print(pomeranian.get_info())
print(shih_tzu.get_info())
print(siberian_husky.get_info())
print(toy_poodle.get_info())
```