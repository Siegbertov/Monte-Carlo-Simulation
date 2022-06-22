from .person import Person, Deck, ActionSpace  # imported DECK with annotation purposes


class Player(Person):
    def __init__(self, threshold=17, strategy=None):
        super().__init__(threshold=threshold, strategy=strategy)

    def make_decision(self) -> list:  # list of ActionSpace(Enum) SPLIT / STAND / HIT
        dec = []
        for hand in self.hands:
            if ActionSpace.SPLIT in hand.possible_actions:
                dec.append(ActionSpace.SPLIT)
            elif hand.best_score >= self.threshold:
                dec.append(ActionSpace.STAND)
            else:
                dec.append(ActionSpace.HIT)
        return dec

    def play(self, deck: Deck):
        while not self.is_stand:
            decisions = self.make_decision()
            hands = self.hands
            new_hands = []

            for i, decision in enumerate(decisions):
                if decision == ActionSpace.SPLIT:
                    new_hand = hands[i].split(deck)
                    new_hands.append(new_hand[0])
                    new_hands.append(new_hand[1])
                elif decision == ActionSpace.HIT:
                    new_hand = hands[i].hit(deck)
                    new_hands.append(new_hand)
                elif decision == ActionSpace.STAND:
                    new_hand = hands[i].stand()
                    new_hands.append(new_hand)
                    self.is_stand = True
            self.hands = new_hands
