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

messages = {
    4: "Create a website using Vuejs",
    7: "Create an app with Flutter",
    8: "Use mongodb for the database in a aglet-webshop",
    9: "Try to make a backend in Go",
    3: "Try to make an iPhone app",
    6: "Create a website using React",
    1: "Create an app with react-native",
    2: "Create a website using Angular"
}

def play():
    color = input("Select a color of the following: "+str(colors)+ "\n").lower()
    if color in colors:
        print("You chose: "+color)
    else:
        print("Invalid color")
        play()
    
    print(f"{color} is {len(color)} characters long")
    for i in range(len(color)):
        if i % 2 == 0:
            print("Nip")
        else:
            print("Nap")
    
    nums = map(lambda x: x[len(color) % 2], numbers.values())
    number = input("Select a number of the following: "+str(nums)+ "\n")
    if number in nums:
        print("You chose: "+number)
    else:
        print("Invalid number")
        play()

    for i in range(number):
        if i % 2 == 0:
            print("Nip")
        else:
            print("Nap")
    
    nums = map(lambda x: x[(len(color) + number)  % 2], numbers.values())
    final = input("Select a number of the following: "+str(nums)+ "\n")
    if final in nums:
        print("You chose: "+final)

        print(messages[color][len(color) % 2])
    else:
        print("Invalid number")
        play()
    


if __name__ == '__main__':
    while True:
        play()
        i = input("Would you like to play again? (Y/n)")
        if i.lower() == 'n':
            break