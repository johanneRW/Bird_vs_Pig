import random


class Bird:
    direction_dict_left = {'n': 'w', 'w': 's', 's': 'e', 'e': 'n'}
    direction_dict_right = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}

    def __init__(self, currentPosition):
        self.currentPosition = currentPosition
        self.direction = 'e'

    def turn_left(self):
        self.direction = self.direction_dict_left[self.direction]

    def turn_right(self):
        self.direction = self.direction_dict_right[self.direction]

    def forward(self):
        if self.direction == 'e':
            self.currentPosition = self.currentPosition[0], self.currentPosition[1] + 1
        if self.direction == 'w':
            self.currentPosition = self.currentPosition[0], self.currentPosition[1] - 1
        if self.direction == 's':
            self.currentPosition = self.currentPosition[0] + 1, self.currentPosition[1]
        if self.direction == 'n':
            self.currentPosition = self.currentPosition[0] - 1, self.currentPosition[1]


class Pig:

    def __init__(self, position):
        self.position = position


class Board:

    def __init__(self, number):
        self.number = number
        self.bird = Bird(self.get_random_position())
        self.pig = Pig(self.get_random_position())

    def get_random_position(self):
        return (random.randint(0, self.number - 1),
                random.randint(0, self.number - 1))

    def display_board(self):
        for i in range(self.number):
            for j in range(self.number):
                char = '* '
                if (i, j) == self.bird.currentPosition:
                    char = 'B '
                if (i, j) == self.pig.position:
                    char = 'P '
                print(char, end='')
            print()

    def run(self, commands):
        for command in commands:
            if command == 'f':
                self.bird.forward()
            if command == 'l':
                self.bird.turn_left()
            if command == 'r':
                self.bird.turn_right()
        return self.bird.currentPosition, self.pig.position


class Workspace:

    def take_input(self):
        result = []
        finished = False
        while not finished:
            comand = input('Move:')
            if comand == 'q':
                finished = True
            else:
                result.append(comand)
        return result

    def hurray(self, bird, pig):
        print("Hurray!! You hit the pig")
        print("Bird Position: ", bird)
        print("Pig Position: ", pig)

    def sorry(self, bird, pig):
        print("Sorry, you did not hit the pig.. ")
        print("Bird Position: ", bird)
        print("Pig Position: ", pig)

    def instructions(self):
        print("""What steps do you want to preform?
        Options: Move forward (f), turn left(l), turn right (r)
        Type (q) when finished""")


class Game:

    def __init__(self):
        workspace = Workspace()
        board = Board(10)
        board.display_board()
        workspace.instructions()
        commands = workspace.take_input()
        bird, pig = board.run(commands)
        if bird == pig:
            workspace.hurray(bird, pig)
        else:
            workspace.sorry(bird, pig)


Game()
