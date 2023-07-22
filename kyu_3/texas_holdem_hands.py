########################################################################################################################
# Texas Hold'em is a Poker variant in which each player is given two "hole cards".
# Players then proceed to make a series of bets while five "community cards" are dealt.
# If there are more than one player remaining when the betting stops, a showdown takes place
# in which players reveal their cards. Each player makes the best poker hand possible using five
# of the seven available cards (community cards + the player's hole cards).
#
# Possible hands are, in descending order of value:
#
#     1) Straight-flush (five consecutive ranks of the same suit). Higher rank is better.
#     2) Four-of-a-kind (four cards with the same rank). Tiebreaker is first the rank,
#        then the rank of the remaining card.
#     3) Full house (three cards with the same rank, two with another).
#        Tiebreaker is first the rank of the three cards, then rank of the pair.
#     4) Flush (five cards of the same suit). Higher ranks are better, compared from high to low rank.
#     5) Straight (five consecutive ranks). Higher rank is better.
#     6) Three-of-a-kind (three cards of the same rank). Tiebreaker is first the rank of the three cards,
#        then the highest other rank, then the second-highest other rank.
#     7) Two pair (two cards of the same rank, two cards of another rank). Tiebreaker is first the rank of
#        the high pair, then the rank of the low pair and then the rank of the remaining card.
#     8) Pair (two cards of the same rank). Tiebreaker is first the rank of the two cards, then the three other ranks.
#     9) Nothing. Tiebreaker is the rank of the cards from high to low.
#
# Given hole cards and community cards, complete the function hand to return the type of hand (as written above,
# you can ignore case) and a list of ranks in decreasing order of significance,
# to use for comparison against other hands of the same type, of the best possible hand.
########################################################################################################################
from collections import Counter

CARDS = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
CARD_RANKS = {card: pos for pos, card in enumerate(CARDS, start=2)}


def _check_if_consecutive(cards: list) -> list:
    """Returns first 5 cards that are consecutive, otherwise an empty list."""
    cards = list(set(cards))
    cards.sort(key=lambda x: CARD_RANKS[x], reverse=True)
    if len(cards) < 5:
        return []

    consecutive = 0
    for i in range(len(cards) - 1):
        diff = CARD_RANKS[cards[i]] - CARD_RANKS[cards[i + 1]]
        if diff == 1:
            consecutive += 1
            if consecutive == 4:
                return cards[i - 3: i + 2]
        else:
            consecutive = 0
            if len(cards) - i <= 5:
                return []


def _check_if_same_color(cards: list) -> list:
    """Returns the list of the values that have the same color.
     If quantity of those is less than 5, returns an empty list."""
    color_counter = Counter([card[-1] for card in cards])
    color, occurrence = color_counter.most_common(1)[0]
    if occurrence >= 5:
        return [card[:-1] for card in cards if card.endswith(color)]

    return []


def _check_repetitions(cards: list) -> list:
    """Returns 4 cards with most repetitions."""
    value_counter = Counter(cards)
    return value_counter.most_common(4)


def hand(hole_cards: list, community_cards: list) -> tuple:
    cards = hole_cards + community_cards
    cards.sort(key=lambda x: CARD_RANKS[x[:-1]], reverse=True)
    same_color_cards = _check_if_same_color(cards=cards)
    cards = [card[:-1] for card in cards]
    most_common = _check_repetitions(cards=cards)
    if same_color_cards:
        consecutive = _check_if_consecutive(cards=same_color_cards)
    else:
        consecutive = _check_if_consecutive(cards=cards)

    if same_color_cards and consecutive:
        return 'straight-flush', consecutive

    if most_common[0][1] == 4:
        return 'four-of-a-kind', [most_common[0][0], most_common[1][0]]

    if most_common[0][1] == 3 and most_common[1][1] == 2:
        return 'full house', [most_common[0][0], most_common[1][0]]

    if same_color_cards:
        return 'flush', same_color_cards[:5]

    if consecutive:
        return 'straight', consecutive

    if most_common[0][1] == 3:
        return 'three-of-a-kind', [most_common[0][0], most_common[1][0], most_common[2][0]]

    if most_common[0][1] == 2 and most_common[1][1] == 2:
        return 'two pair', [most_common[0][0], most_common[1][0], most_common[2][0]]

    if most_common[0][1] == 2:
        return 'pair', [most_common[0][0], most_common[1][0], most_common[2][0], most_common[3][0]]

    return 'nothing', cards[:5]


if __name__ == '__main__':
    print(hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]))
    print(hand(["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"]))
