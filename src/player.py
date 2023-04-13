from PIL import Image, ImageDraw, ImageFont


class Player(object):
    def __init__(self, name, pos):
        self.__name: str = name
        self.__alive: bool = True

        self.__pos: tuple[int] = pos

    def advance(self):
        pass

    def draw(self):
        pass

    def __repr__(self):
        return '[{name}, {status}, {pos}]'.format(name=self.__name, status=self.__alive, pos=self.__pos)
