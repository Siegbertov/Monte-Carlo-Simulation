from .person import Person, Deck, ActionSpace


class Dealer(Person):
    def __init__(self, threshold=17, strategy=None):
        super().__init__(threshold=threshold, strategy=strategy)

    def get_visible_card(self):
        """return first card from its hand"""
        return self.hands[0][0]

    def play(self, deck: Deck):
        while not self.is_stand:
            decisions = self.make_decision()
            hands = self.hands
            new_hands = []

            for i, decision in enumerate(decisions):
                if decision == ActionSpace.HIT:
                    new_hand = hands[i].hit(deck)
                    new_hands.append(new_hand)
                elif decision == ActionSpace.STAND:
                    new_hand = hands[i].stand()
                    new_hands.append(new_hand)
                    self.is_stand = True
            self.hands = new_hands

