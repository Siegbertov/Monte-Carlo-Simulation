from .action import ActionSpace
from .card import Card   # imported with annotation purposes
from .deck import Deck  # imported with annotation purposes


class Hand:
    GOAL = 21

    def __init__(self):
        self.cards = []

        self.score_space = None
        self.best_score = None
        self.possible_actions = None

    def show(self):
        print(f"{self.cards} ===> {self.best_score} ===> {self.score_space}")

    def put(self, card: Card):
        self.cards.append(card)
        self.count()

    def __getitem__(self, item):
        return self.cards.__getitem__(item)

    def __len__(self):
        return self.cards.__len__()

    def count(self):
        self._count_score_space()
        self._count_best_score()
        self._count_possible_actions()

    def split(self, deck: Deck):
        h1 = Hand()
        h2 = Hand()

        h1.put(self[0])
        h1.put(deck.pop_one_card())

        h2.put(self[1])
        h2.put(deck.pop_one_card())
        return h1, h2

    def hit(self, deck: Deck):
        self.put(deck.pop_one_card())
        return self

    def stand(self):
        return self

    def _count_score_space(self):
        scores = [c.get_score() for c in self.cards]
        first_score = scores[0]
        for next_score in scores[1:]:
            if type(first_score) == int:
                if type(next_score) == int:
                    first_score += next_score

                elif type(next_score) == tuple:
                    new_s = []
                    for s in next_score:
                        new_s.append(first_score+s)
                    first_score = tuple(set(new_s))

            elif type(first_score) == tuple:
                if type(next_score) == int:
                    new_s = []
                    for s in first_score:
                        new_s.append(next_score + s)
                    first_score = tuple(set(new_s))

                elif type(next_score) == tuple:
                    new_s = []
                    for f_s in first_score:
                        for n_s in next_score:
                            new_s.append(f_s + n_s)
                    first_score = tuple(set(new_s))

        if isinstance(first_score, tuple):
            first_score = tuple(sorted(first_score))
        self.score_space = first_score

    def _count_best_score(self):
        if type(self.score_space) == int:
            self.best_score = self.score_space
        else:
            self.best_score = self.score_space[0]
            for next_score in self.score_space[1:]:
                if next_score <= self.GOAL:
                    self.best_score = next_score
                else:
                    break

    def _count_possible_actions(self):
        possible_actions = [ActionSpace.STAND, ActionSpace.HIT]
        if self._can_be_split():
            possible_actions.append(ActionSpace.SPLIT)
        self.possible_actions = possible_actions

    def _can_be_split(self) -> bool:
        return True if len(self.cards) == 2 and self.cards[0].rank == self.cards[1].rank else False
