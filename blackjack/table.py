from .player import Player
from .dealer import Dealer
from .deck import Deck
from .person import Person  # imported with annotation purposes
from .champion import ChampionSpace


class Table:
    GOAL = 21

    def __init__(self, player_strategy=None, dealer_threshold=17, player_threshold=17):
        self.player_threshold = player_threshold
        self.dealer_threshold = dealer_threshold

        self.player = Player(threshold=player_threshold, strategy=player_strategy)
        self.dealer = Dealer(threshold=dealer_threshold)
        self.deck = Deck()
        self._start()

    def reset(self):
        self.player.reset()
        self.dealer.reset()
        self.deck.reset()
        self._start()

    def _give_on_start(self, person: Person):
        person.take(self.deck.pop_one_card())

    def _start(self):
        for _ in range(2):
            self._give_on_start(self.player)
            self._give_on_start(self.dealer)

    def show(self):
        print("PLAYER")
        self.player.show()
        print()
        print("DEALER")
        self.dealer.show()

    def play(self):
        self.player.play(self.deck)
        self.dealer.play(self.deck)

    def who_win(self):
        player_scores = [hand.best_score for hand in self.player.hands]
        dealer_score = self.dealer.hands[0].best_score
        results = []

        for player_score in player_scores:
            if player_score < self.GOAL:
                if dealer_score < self.GOAL:
                    if player_score == dealer_score:
                        results.append(ChampionSpace.DRAW)
                    elif player_score > dealer_score:
                        results.append(ChampionSpace.PLAYER)
                    else:
                        results.append(ChampionSpace.DEALER)
                elif dealer_score == self.GOAL:
                    results.append(ChampionSpace.DEALER)
                elif dealer_score > self.GOAL:
                    results.append(ChampionSpace.PLAYER)

            elif player_score == self.GOAL:
                if dealer_score < self.GOAL:
                    results.append(ChampionSpace.PLAYER)
                elif dealer_score == self.GOAL:
                    results.append(ChampionSpace.DRAW)
                elif dealer_score > self.GOAL:
                    results.append(ChampionSpace.PLAYER)

            elif player_score > self.GOAL:
                if dealer_score < self.GOAL:
                    results.append(ChampionSpace.DEALER)
                elif dealer_score == self.GOAL:
                    results.append(ChampionSpace.DEALER)
                elif dealer_score > self.GOAL:
                    if player_score == dealer_score:
                        results.append(ChampionSpace.DRAW)
                    elif player_score < dealer_score:
                        results.append(ChampionSpace.PLAYER)
                    else:
                        results.append(ChampionSpace.DEALER)

        return results
