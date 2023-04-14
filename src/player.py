from PIL import Image, ImageDraw, ImageFont


class Player(object):
    font = ImageFont.truetype('../fonts/Main-font.TTF', size=65)
    color: str = 'white'
    strokeWidth: int = 5
    strokeColor: str = 'black'

    def __init__(self, name: str, pos: tuple[int, int], img: Image.Image):
        self.__name: str = name
        self.alive: bool = True

        self.__pos: tuple[int, int] = pos
        self.__draw = ImageDraw.Draw(img)

    def draw(self):
        self.__draw.text(xy=self.__pos, text=self.__name, fill=Player.color,
                         font=Player.font, stroke_fill=Player.strokeColor, stroke_width=Player.strokeWidth)

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return '{{{name}, {status}}}'.format(name=self.__name, status=self.alive)
