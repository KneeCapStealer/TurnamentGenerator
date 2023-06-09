from player import Player
import UIManager as Ui
import random
import Util


def main():
    img = Util.load_image('../images/smash_turnering.png')

    # these positions were found by hand, ew
    startPositions = ((200, 600), (200, 827), (200, 1054), (200, 1281),
                      (2170, 600), (2170, 827), (2170, 1054), (2170, 1281))

    semiPositions = ((750, 702), (750, 1159), (1702, 702), (1702, 1159))
    finalPositions = ((1114, 930), (1343, 930))
    winnerPos = ((1225, 800), )

    roundPos = (semiPositions, finalPositions, winnerPos)

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

    pairs = Util.generate_pairs(players)

    for player in players:
        player.draw()

    img.show()
    for roundNum in range(3):

        for fightNum, pair in enumerate(pairs):
            if len(pair) < 2:
                if roundNum == 2:
                    print(f'The winner is {pair[0].name}')

                    Util.draw_chall_num(roundPos[2][0], players.index(pair[0]) + 1, img)
                    img.save('../modImg/tournament.png', 'PNG')
                    break

                print('\nThere is only a single challenger remaining, skipping to next round')
                Util.draw_chall_num(roundPos[roundNum][fightNum], players.index(pair[0])+1, img)
                img.save('../modImg/tournament.png', 'PNG')
                pairs = Util.generate_pairs([player for player in players if player.alive])
                break

            print('\nchallenger number {one} \'{name1}\' and {two} \'{name2}\' are fighting now'
                  .format(one=players.index(pair[0])+1, two=players.index(pair[1])+1,
                          name1=pair[0].name, name2=pair[1].name))

            # Keep asking for the winning challenger until a correct number is entered and the action is verified
            while True:
                winner = Util.int_input('Please type which challenger won the battle here ({one} or {two}): '
                                        .format(one=players.index(pair[0])+1, two=players.index(pair[1])+1))

                # Make sure the input is correct
                if winner != players.index(pair[0])+1 and winner != players.index(pair[1])+1:
                    print('Needs to be challenger {one} or {two}'
                          .format(one=players.index(pair[0])+1, two=players.index(pair[1])+1))
                    continue

                # Verify answer and set the loosing player to {player.alive = False}
                if input(f'Are you sure challenger {winner} won? y/n ') == 'y':
                    for player in pair:
                        player.alive = False

                    players[winner - 1].alive = True
                    break

            # if It's the last
            if roundNum == 2:
                print(f'The winner is {players[winner-1].name}')

            Util.draw_chall_num(roundPos[roundNum][fightNum], winner, img)
            img.save('../modImg/tournament.png', 'PNG')

        else:
            print('No more challengers remaining, going to the next round')
            pairs = Util.generate_pairs([player for player in players if player.alive])


if __name__ == "__main__":
    test = Ui.UIManager()
    main()
