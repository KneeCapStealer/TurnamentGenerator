from PIL import Image, ImageDraw, ImageFont
from player import *
import random
import Util


def main():
    img = Util.load_image('../images/smash_turnering.png')

    # these positions were found by hand, ew
    startPositions = [(200, 600), (200, 827), (200, 1054), (200, 1281),
                      (2170, 600), (2170, 827), (2170, 1054), (2170, 1281)]

    semiPositions = [(750, 707), (750, 1164), (1702, 707), (1702, 1164)]
    # finalPositions = [(1114, 935), (1343, 935)]

    while True:
        names = input("Hello, please type in player names like so:(name1, name2, name3, ...): ").split(", ")

        if len(names) > 8:
            print("Please dont exceed 8 players, try again")
        else:
            random.shuffle(names)
            break

    players = []
    for i, name in enumerate(names):
        players.append(Player(name, startPositions[i], img))

    print(f'{names=}')
    print(f'{players=}')

    pairs = Util.generate_pairs(players)
    print(f'\n{pairs=}')

    while True:
        for player in players:
            player.draw()

        img.show()

        for fightNum, pair in enumerate(pairs):
            print('pair size: {}'.format(len(pair)))
            if len(pair) < 2:
                print('There is only a single challenger remaining, skipping to next round')
                Util.draw_chall_num(semiPositions[fightNum], fightNum * 2 + 1, img)
                pairs = Util.generate_pairs([player for player in players if player.alive])
                break

            print('challenger number \'{one}\' and \'{two}\' are fighting now'
                  .format(one=fightNum * 2 + 1, two=fightNum * 2 + 2))

            while True:
                winner = Util.int_input('\nPlease type which challenger won the battle here ({one} or {two}): '
                                        .format(one=fightNum * 2 + 1, two=fightNum * 2 + 2))

                if winner != fightNum * 2 + 1 and winner != fightNum * 2 + 2:
                    print('Needs to be challenger {one} or {two}'.format(one=fightNum * 2 + 1, two=fightNum * 2 + 2))
                    continue

                if input(f'Are you sure challenger {winner} won? y/n ') == 'y':
                    break

            Util.draw_chall_num(semiPositions[fightNum], winner, img)

            img.show()

        else:
            print('No more challengers remaining, skipping to the next round')
            pairs = Util.generate_pairs([player for player in players if player.alive])


if __name__ == "__main__":
    main()
