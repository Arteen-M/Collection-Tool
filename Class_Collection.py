class Console:
    def __init__(self, console):
        self.console = console
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def remove_game(self, game):
        if game in self.games:
            self.games.remove(game)

    def show_games(self):
        for game in self.games:
            print(game)

    def sort_list(self):
        self.games.sort()

    def find_game(self, name):
        if name in self.games:
            print(True)


def Convert(string):
    li = list(string.split(","))
    return li


try:
    file = open("Database.txt", "r")
    file.close()
except FileNotFoundError:
    file = open("Database.txt", "w")
    file.close()

file = open("Database.txt", "r")

f = []
console_list = []
games_list = None

for x in range(1, 20):
    f += file.readlines(x)

for x in range(len(f)):
    console_list.append(Console(f[x][:f[x].find("[")]))
    games_list = f[x][f[x].find("[") + 1:f[x].find("]") - 1].replace("\'", "").replace(", ", ",").replace('\"', "")
    console_list[x].games = Convert(games_list)
    if '' in console_list[x].games:
        console_list[x].games.remove('')

while True:
    action = input()
    if action[:3].lower() == "add":
        for x in range(len(console_list)):
            if action[4:action[4:].find(" ") + 4] == console_list[x].console:
                console_list[x].add_game(action[action[4:].find(" ") + 5:])
                print("%s added" % action[action[4:].find(" ") + 5:])

    if action[:6].lower() == "remove":
        for x in range(len(console_list)):
            if action[7:action[7:].find(" ") + 7] == console_list[x].console:
                console_list[x].remove_game(action[action[7:].find(" ") + 8:])
                print("%s removed" % action[action[7:].find(" ") + 8:])

    if action[:4].lower() == "show":
        for x in range(len(console_list)):
            if action[5:] == console_list[x].console:
                console_list[x].show_games()

    if action[:4].lower() == "find":
        for x in range(len(console_list)):
            if action[5:action[5:].find(" ") + 5] == console_list[x].console:
                if action[action[5:].find(" ") + 6:] in console_list[x].games:
                    print("Found %s in Collection" % action[action[5:].find(" ") + 6:])
                else:
                    print("Not %s in Collection" % action[action[5:].find(" ") + 6:])

    if action[:4].lower() == "sort":
        for x in range(len(console_list)):
            if action[5:] == console_list[x].console:
                console_list[x].sort_list()
                print(action[5:] + " sorted")

    if action[:6].lower() == "create":
        console_list.append(Console(action[7:]))
        print(action[7:] + " created")

    if action[:6].lower() == "delete":
        for x in range(len(console_list)):
            if action[7:] == console_list[x].console:
                console_list.pop(x)
                print(action[7:] + " deleted")

    if action.lower() == "reset all":
        print("Are you sure? This will delete all records of the collection")
        confirmation = input()
        if confirmation.lower() == "yes" or confirmation.lower() == "y":
            console_list = []

    if action.lower() == "help":
        print("""Create [Name (Console)] - Create a new Group
Delete [Name (Group)] - Remove an existing Group
Show [Name (Group)] - Shows all objects in a Group
Find [Name (Group)] [Name (Object)] - Finds a specific object in a Group (must be exact name)
Sort [Name (Group)] - Sorts by Name the Group
Add [Name (Group)] [Name (Object)] - Adds an Object into a Group
Remove [Name (Group)] [Name (Object)] - Removes an Object from a Group
Reset All - Delete all records
End - Save and quit the program""")

    if action.lower() == "end":
        break


file = open("Database.txt", "w")

for x in range(len(console_list)):
    file.write(str(console_list[x].console))
    file.write(str(console_list[x].games))
    file.write("\n")

file.close()
