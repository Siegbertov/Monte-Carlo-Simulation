from blackjack import Game


def main():
    new_game = Game()
    for _ in range(10_000):
        new_game.play()
        new_game.reset()

    print(new_game.get_not_losing())


if __name__ == "__main__":
    main()
