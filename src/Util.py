from PIL import Image, ImageDraw, ImageFont
from player import Player


# Tries to convert input to int, will repeat forever until valid int is typed
def int_input(msg: str):
    while True:
        try:
            output = int(input(msg))
        except ValueError:
            print('Input needs to be an integer')
        else:
            return output


# Tries to convert input to bool, will repeat forever until valid bool is typed
def bool_input(msg: str):
    while True:
        try:
            output = bool(input(msg))
        except ValueError:
            print('Input needs to be a bool')
        else:
            return output


def draw_chall_num(pos: tuple[int, int], num: int, img: Image.Image):
    ImageDraw.Draw(img).text(xy=pos, text=str(num), fill=Player.color,
                             font=ImageFont.truetype('../fonts/Main-font.TTF', size=80),
                             stroke_fill=Player.strokeColor, stroke_width=Player.strokeWidth)


def generate_pairs(players: list[Player]):
    # Every Odd challenger
    groupA = players[::2]
    # Every Even challenger
    groupB = players[1::2]

    if len(groupA) == len(groupB):
        return tuple(zip(groupA, groupB))
    else:
        tmpZip = list(zip(groupA, groupB))
        tmpZip.append((players[-1],))
        return tuple(tmpZip)


def load_image(filePath: str) -> Image.Image:
    try:
        return Image.open(filePath)

    except OSError:
        print('couldn\'t find Smash tournament image, default is orange screen')
        return Image.new(mode="RGBA", size=(400, 300), color='darkorange')
