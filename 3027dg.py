

print("+------------------+")
print("|  hs game console  |")
print("+------------------+")
print(" ")
print("+--------------------------------+")
print("| 1. games                       |")
print("| 2. instalar hs-studio          |")
print("| 3. loja de game                |")
print("+--------------------------------+")

escolha = input("Escolha uma opção: ")

if escolha == "1":
    print("Iniciando novo jogo...")
  elif escolha == "2":
  import json

def save_game(game_name, game_description):
    with open(f"{game_name}.json", "w") as f:
        game_data = {
            "name": game_name,
            "description": game_description,
            "version": "1.0",
            "author": "Your Name",
            "engine": "Console Game Engine"
        }
        json.dump(game_data, f, indent=4)

def new_game():
    game_name = input("Enter the game name: ")
    game_description = input("Enter the game description: ")
    save_game(game_name, game_description)

def save_features():
    with open("features.txt", "w") as f:
        f.write("Feature 1: ...\n")
        f.write("Feature 2: ...\n")
        f.write("Feature 3: ...\n")

print("+------------------+")
print("|  Console Game Engine |")
print("+------------------+")
print("| 1. New Game       |")
print("| 2. Save Features  |")
print("| 3. Exit           |")
print("+------------------+")

while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        new_game()
    elif choice == "2":
        save_features()
    elif choice == "3":
        print("Exiting the game engine...")
        break
    else:
        print("Invalid choice, try again.")



else:
    print("Opção inválida!")
