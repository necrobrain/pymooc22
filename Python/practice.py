print("Welcome!")

while True: 
    name = input("Give me a name. ")

    if name == "Fen":
        print("Idiot!")

    if name != "Fen":
        break

print("You are not an idiot.")

age = int(input("What was your age in 2017? "))

year = int(input("What year is it now? "))

if year is not 2017:
    age += year - 2017

print(f"You are {age} years old")

word = input("Please type in a word: ")
length = len(word)

if length > 1:
    print(f"There are {length} letters in the word {word}")

print("Thank you!")