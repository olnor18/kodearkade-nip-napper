colors = ["red", "green", "blue", "purple"]
numbers = {
    "red": [4, 7],
    "green": [8, 9],
    "blue": [3, 6],
    "purple": [1, 2]
}

messages = {
    "red": ["Create a website using Vuejs", "Create an app with Flutter"],
    "green": ["Use mongodb for the database in a note-taking app", "Try to make a backend in Go"],
    "blue": ["Try to make an iPhone app", "Create a website using React"],
    "purple": ["Create an app with react-native", "Create a website using Angular"]
}

def play():
    color = input("Select a color of the following: "+str(colors))
    if color.lower() in colors:
        print("You chose: "+color)
    else:
        print("Invalid color")
        play()
    
    for i in range(len(color)):
        if i % 2 == 0:
            print("Nip")
        else:
            print("Nap")
    
    for i in range(numbers[color][len(color) % 2]):
        if i % 2 == 0:
            print("Nip")
        else:
            print("Nap")
    
    print(messages[color][len(color) % 2])


if __name__ == '__main__':
    while True:
        play()
        i = input("Would you like to play again? (Y/n)")
        if i.lower() == 'n':
            break