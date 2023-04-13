from PIL import Image, ImageDraw, ImageFont, ImageColor
from player import *
import random
import math


def load_image(filePath) -> Image:
    try:
        return Image.open(filePath)

    except OSError:
        print('couldn\'t find Smash tournament image, you might want to restart program')
        return Image.new(mode="RGBA", size=(400,300), color='darkorange')


def generate_pairs(players: tuple[Player]) -> tuple[tuple[Player]]:
    pass


def main():
    img = load_image('../images/smash_turnering.png')

    while True:
        names = input("Hello, please type in player names like so:(name1, name2, name3, ...): ").split(", ")

        if len(names) < 8:
            print("Please dont exceed 8 players, try again")
        else:
            break

    startPositions = [(100, 250), (350, 450)]
    random.shuffle(startPositions)
    semiPositions = [(), (), (), ()]
    finalPositions = [(), ()]

    players = []
    for i, name in enumerate(names):
        players.append(Player(name, startPositions[i]))

    print(f'{names=}')
    print(f'{players=}')

    # for each pair of players
    for i in range(math.floor(len(players)/2)):
        pass


if __name__ == "__main__":
    main()
