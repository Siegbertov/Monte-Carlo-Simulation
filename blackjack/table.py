from .card import Card
from .player import Player
from .dealer import Dealer
from random import shuffle

from .action import ActionSpace
from .champion import ChampionSpace


class Table:
    GOAL = 21
    POSSIBLE_SUITS_U = ['♠', '♥', '♦', '♣']
    POSSIBLE_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, player_threshold, dealer_threshold):
        self.player_threshold = player_threshold
        self.dealer_threshold = dealer_threshold

        self.main_player = Player(player_threshold)
        self.main_dealer = Dealer(dealer_threshold)

        self.deck = []
        self._create_deck()
        self.start()

    def _create_deck(self):
        for s in self.POSSIBLE_SUITS_U:
            for r in self.POSSIBLE_RANKS:
                self.deck.append(Card(s, r))
        self._shuffle_deck()

    def reset(self):
        self.main_player.reset()
        self.main_dealer.reset()

        self.deck = []
        self._create_deck()
        self.start()

    def _shuffle_deck(self):
        shuffle(self.deck)

    def _give_card(self, who):
        who.take(self.deck.pop())
        who.count_score_space()

    def start(self):
        for _ in range(2):
            self._give_card(self.main_player)
            self._give_card(self.main_dealer)

    def who_won(self):
        player_score = self.main_player.best_score
        dealer_score = self.main_dealer.best_score

        if player_score < self.GOAL:
            if dealer_score < self.GOAL:
                return ChampionSpace.DRAW if player_score == dealer_score else ChampionSpace.PLAYER if player_score > dealer_score else ChampionSpace.DEALER
            elif dealer_score == self.GOAL:
                return ChampionSpace.DEALER
            elif dealer_score > self.GOAL:
                return ChampionSpace.PLAYER

        elif player_score == self.GOAL:
            if dealer_score < self.GOAL:
                return ChampionSpace.PLAYER
            elif dealer_score == self.GOAL:
                return ChampionSpace.DRAW
            elif dealer_score > self.GOAL:
                return ChampionSpace.PLAYER

        elif player_score > self.GOAL:
            if dealer_score < self.GOAL:
                return ChampionSpace.DEALER
            elif dealer_score == self.GOAL:
                return ChampionSpace.DEALER
            elif dealer_score > self.GOAL:
                return ChampionSpace.DRAW if player_score == dealer_score else ChampionSpace.PLAYER if player_score < dealer_score else ChampionSpace.DEALER

    def play(self):
        # PLAYER TAKES ACTIONS
        while not self.main_player.is_stand:
            decision = self.main_player.make_decision(self.main_dealer.get_visible_card())
            if decision == ActionSpace.HIT:
                self._give_card(self.main_player)
            elif decision == ActionSpace.STAND:
                self.main_player.is_stand = True

        # DEALER TAKES ACTIONS
        while not self.main_dealer.is_stand:
            decision = self.main_dealer.make_decision()
            if decision == ActionSpace.HIT:
                self._give_card(self.main_dealer)
            elif decision == ActionSpace.STAND:
                self.main_dealer.is_stand = True
