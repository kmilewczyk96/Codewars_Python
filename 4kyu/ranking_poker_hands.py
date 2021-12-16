########################################################################################################################
# A famous casino is suddenly faced with a sharp decline of their revenues.
# They decide to offer Texas hold'em also online. Can you help them by writing an algorithm that can rank poker hands?
#
# Task
# Create a poker hand that has a method to compare itself to another poker hand:
#
# compare_with(self, other_hand)
# A poker hand has a constructor that accepts a string containing 5 cards:
#
# PokerHand("KS 2H 5C JD TD")
# The characteristics of the string of cards are:
#
# Each card consists of two characters, where
# The first character is the value of the card: 2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
# The second character represents the suit: S(pades), H(earts), D(iamonds), C(lubs)
# A space is used as card separator between cards
# The result of your poker hand compare can be one of these 3 options:
#
# [ "Win", "Tie", "Loss" ]
# Notes
# Apply the Texas Hold'em rules for ranking the cards.
# Low aces are NOT valid in this kata.
# There is no ranking for the suits.
########################################################################################################################
from collections import Counter


class PokerHand(object):
    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, hand: str):
        self.hand = hand.split()
        self.alpha_values = {
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        self.hands_rank = {
            "ROYAL_FLUSH": 9,
            "STRAIGHT_FLUSH": 8,
            "FOUR_OF_A_KIND": 7,
            "FULL_HOUSE": 6,
            "FLUSH": 5,
            "STRAIGHT": 4,
            "THREE_OF_A_KIND": 3,
            "TWO_PAIR": 2,
            "PAIR": 1,
            "NONE": 0
        }

    def get_hand(self):
        return self.hand

    def get_value(self, card: str):
        return self.alpha_values.get(card[0])

    def hand_values(self):
        values = []
        for card in self.get_hand():
            if card[0].isnumeric():
                values.append(int(card[0]))
            else:
                values.append(self.get_value(card))

        values.sort(reverse=True)
        return values

    def hand_colors(self):
        colors = set()
        for card in self.get_hand():
            colors.add(card[1])

        return colors

    def check_for_sequence(self):
        for i in range(4):
            if self.hand_values()[i + 1] != self.hand_values()[i] - 1:
                return False

        return True

    def check_suit(self):
        if len(self.hand_colors()) != 1:
            return False

        return True

    def check_for_repetition(self):
        repetitions = Counter(self.hand_values())
        return [i for i in sorted(repetitions.values()) if i != 1]

    def check_hand(self):
        if self.check_suit():
            if self.check_for_sequence():
                if self.hand_values()[0] == 14:
                    return "ROYAL_FLUSH"

                return "STRAIGHT_FLUSH"

            return "FLUSH"

        else:
            if self.check_for_sequence():
                return "STRAIGHT"

            else:
                if self.check_for_repetition() == [4]:
                    return "FOUR_OF_A_KIND"
                elif self.check_for_repetition() == [2, 3]:
                    return "FULL_HOUSE"
                elif self.check_for_repetition() == [3]:
                    return "THREE_OF_A_KIND"
                elif self.check_for_repetition() == [2, 2]:
                    return "TWO_PAIR"
                elif self.check_for_repetition() == [2]:
                    return "PAIR"

                return "NONE"

    def tie_solver(self):
        ordered = Counter(self.hand_values())
        return [i[0] for i in ordered.most_common()]

    def compare_with(self, other):
        result = self.hands_rank.get(self.check_hand()) - \
                 self.hands_rank.get(other.check_hand())

        if result > 0:
            return self.RESULT[2]

        elif result < 0:
            return self.RESULT[0]

        else:
            for i in range(len(self.tie_solver())):
                if self.tie_solver()[i] > other.tie_solver()[i]:
                    return self.RESULT[2]
                elif self.tie_solver()[i] < other.tie_solver()[i]:
                    return self.RESULT[0]

            return self.RESULT[1]


if __name__ == '__main__':
    player = PokerHand('2S 3S 4S 5S 6S')
    opponent = PokerHand('TS JS JD 5C 5C')

    print(player.compare_with(opponent))
