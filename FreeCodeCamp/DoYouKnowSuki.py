# name and age
name = input("Hi, what's your name? ")
print("Hello, " + name + "!", "Nice to meet you!")

while True:
    age = input("How old are you? ")
    if age.isdigit():
        int_age = int(age)
        older = int_age - 11
        if older > 0:
            print("Ah, that's", older, "years older than Suki!")
        if older == 0:
            print("Ah, that's the same age as Suki!")
        if older < 0: 
            older = older * -1
            print("Ah, that's", older, "years younger than Suki!")
        break
    else:
        print("I'm sorry, I didn't understand that. Please type a number!")
        continue

# Know Suki
while True:
    Know = input("Do you know Suki? ")
    if Know == "Yes":
        print("That's great! Suki is the cutest cat in the world!")
        break
    if Know == "yes":
        print("That's great! Suki is the cutest cat in the world!")
        break
    if Know == "No":
        print("You should meet her! She's the cutest cat in the world!")
        break
    if Know == "no":  
        print("You should meet her! She's the cutest cat in the world!")
        break
    else:
        print("I'm sorry, I didn't understand that. Please type 'Yes' or 'No'!")
        continue