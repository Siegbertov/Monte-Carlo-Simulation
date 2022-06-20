from card import Card
from action import ActionSpace


class Person:
    GOAL = 21

    def __init__(self, threshold=17):
        self.threshold = threshold
        self.hand = []
        self.score_space = None
        self.best_score = None
        self.is_stand = False

    def take(self, some_card: Card):
        self.hand.append(some_card)

    def count_score_space(self):
        scores = [c.get_score() for c in self.hand]
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
        self.score_space = first_score
        self._count_best_score()

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

    def show(self):
        print(self.hand, self.best_score)

    def make_decision(self, *args, **kwargs):
        if self.best_score >= self.threshold:
            return ActionSpace.STAND
        else:
            return ActionSpace.HIT
